from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.core.tools import FunctionTool
from llama_index.core import PromptTemplate

from card_tool import *
from article_service import *
from link_tool import *

llm_model_name = "custom_llama_llm" #"llama3.1"
 
def init_llm(): 
    Settings.llm = Ollama(model=llm_model_name, request_timeout=1000.0, base_url = "http://ollama-docker:11434", temperature=0)

def predict_next_card(cards: list[int]):
    current_number = cards.pop(0)

    print(cards)

    play_without_special_cards = list(filter(lambda p: p > 0 and p != 2 and p != 10, cards))
    special_cards = list(filter(lambda p: p == 2 or p == 10, cards))

    alpaca_prompt  = f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    Find the smallest integer in the playlist that is greater than or equal to the current play. If no such number exists, return 0.

    ### Input:
    \"play_list\":{play_without_special_cards} \"current_play\": {current_number}
"""
    
    alpaca_prompt_special_cards = f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    Find the smallest integer in the playlist that is greater than or equal to the current play. If no such number exists, return 0.

    ### Input:
    \"play_list\":{special_cards} \"current_play\": {2}"""

    result = "0" 

    if len(play_without_special_cards) > 0:
        res = Settings.llm.predict(prompt=PromptTemplate(alpaca_prompt), verbose = True)
        print(f"current card: {current_number}")
        print(f"result{res}")
        result = res.split("Response:")[1].strip()

    if int(result) == 0 and len(special_cards) > 0:
        print("checking specal cards")
        res2 = Settings.llm.predict(prompt=PromptTemplate(alpaca_prompt_special_cards), verbose = True)
        print(special_cards)
        print(f"special card response: {res2}")
        result = res2.split("Response:")[1].strip()
    
    return result
