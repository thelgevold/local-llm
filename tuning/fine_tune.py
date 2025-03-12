from unsloth import FastLanguageModel
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported
from datasets import Dataset
import pandas as pd
import json, yaml
import torch

max_seq_length = 1024 
dtype = None 

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "meta-llama/Llama-3.1-8B",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit=True
)

alpaca_prompt_regular_cards  = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Find the smallest integer in the playlist that is greater than or equal to the current play. If no such number exists, return 0.

### Input:
{}

### Response:
{}"""

EOS_TOKEN = tokenizer.eos_token

def formatting_prompts_func_regular_cards(examples):
    inputs       = examples["input"]
    outputs      = examples["output"]
    texts = []
    for input, output in zip(inputs, outputs):
        text = alpaca_prompt_regular_cards.format(input, output) + EOS_TOKEN
        texts.append(text)
    return { "text" : texts, }

with open('/usr/tuning/output.json', 'r') as f:
    json_f = yaml.safe_load(f.read())

df1 = pd.DataFrame(json_f)
dataset = Dataset.from_pandas(df1)
dataset = dataset.map(formatting_prompts_func_regular_cards, batched = True,)

model = FastLanguageModel.get_peft_model(
    model,
    r=16, 
    target_modules=[
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj"
    ],
    lora_alpha=16,
    lora_dropout=0, 
    bias="none", 
    
    use_gradient_checkpointing="unsloth", 
    random_state=3407,
    use_rslora=False, 
    loftq_config=None,
)

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = False,
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        per_device_eval_batch_size = 2,
        gradient_accumulation_steps = 4,
        eval_accumulation_steps = 4,
        warmup_steps = 5,
        num_train_epochs = 150,
        max_steps = 150,
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "/usr/tuning/outputs",
    ),
    train_dataset = dataset
)

trainer_stats = trainer.train()

model.save_pretrained("lora_model")
tokenizer.save_pretrained("lora_model")

model.save_pretrained_gguf("model", tokenizer, maximum_memory_usage = 0.3)


FastLanguageModel.for_inference(model)
inputs1 = tokenizer(
[
    alpaca_prompt_regular_cards.format(
        #"Find the smallest integer in the playlist that is greater than or equal to the current play. If no such number exists, return 0.", # instruction
        "{\"play_list\": [5, 5, 7, 12], \"current_play\": 5}", # input
        "", # output - leave this blank for generation!
    )
], return_tensors = "pt").to("cuda")

outputs = model.generate(**inputs1, max_new_tokens = 500, use_cache = True)
generated1 = tokenizer.batch_decode(outputs)

print(generated1)
