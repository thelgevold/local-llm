from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.core import PromptTemplate

from prompt import prompt_template

llm_model_name = "custom_llama_llm"
 
def init_llm(): 
    Settings.llm = Ollama(model=llm_model_name, request_timeout=1000.0, base_url = "http://ollama-docker:11434", temperature=0)

def predict_next_card(cards: list[int]):
    current_card = cards.pop(0)

    print(cards)

    play_without_special_cards = list(filter(lambda p: p > 0 and p != 2 and p != 10, cards))
    special_cards = list(filter(lambda p: p == 2 or p == 10, cards))

    result = "0" 

    if len(play_without_special_cards) > 0:
        result = predict(play_without_special_cards, current_card)

    if int(result) == 0 and len(special_cards) > 0:
        result = predict(special_cards, 2)
    
    return result

def predict(cards, current_card):
    prompt = prompt_template(cards, current_card)
    res = Settings.llm.predict(prompt=PromptTemplate(prompt), verbose = True)
    print(f"current card: {current_card}")
    print(f"result{res}")
    return res.split("Response:")[1].strip()  
