from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.core.tools import FunctionTool
from llama_index.core import PromptTemplate

from card_tool import *
from article_service import *
from link_tool import *

llm_model_name = "custom_llama" #"llama3.1"
 
def init_llm(): 
    Settings.llm = Ollama(model=llm_model_name, request_timeout=1000.0, base_url = "http://ollama-docker:11434", temperature=0) #, context_window=22000

def predict_next_card(cards: list[int]):
    current_number = cards.pop(0)

    print(cards) 

    play_without_special_cards = filter(lambda p: p > 0 and p != 2 and p != 10, cards)
    special_cards = filter(lambda p: p == 2 or p == 10, cards)

    alpaca_prompt  = f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    Find the smallest integer in the playlist that is greater than or equal to the current play. If no such number exists, return 0.

    ### Input:
    \"play_list\":{list(play_without_special_cards)} \"current_play\": {current_number}
"""
    
    alpaca_prompt_special_cards = f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    Given an array of numbers, your task is to select the first occurrence of either a 2 or a 10. If both exist, select the 2 (giving priority to 2 over 10). If neither 2 nor 10 is found in the array, return 0.

    ### Input:
    {list(special_cards)}"""

    print(special_cards)
    res = Settings.llm.predict(prompt=PromptTemplate(alpaca_prompt), verbose = True)

    print(f"current card: {current_number}")
    print(f"result{res}")
    result = res.split("Response:")[1].strip()

    if int(result) == 0:
        print("checking specal cards")
        res2 = Settings.llm.predict(prompt=PromptTemplate(alpaca_prompt_special_cards), verbose = True)
        result = res2.split("Response:")[1].strip()
    
    return result


def predict_with_external_link(prompt: str):
    tool = FunctionTool.from_defaults(fn=make_http_request, name="get_link_info")
   
    res = Settings.llm.predict_and_call([tool], prompt, verbose = True)
  
    return Settings.llm.predict(prompt=PromptTemplate(res.response))

def predict(title: str):
    article = get_article(title=title)
        
    tool = FunctionTool.from_defaults(fn=get_country_border_info, name="get_country_border_info")
   
    prompt = f"Get information about {title} based on {article}. Rely only on the provided document when generating the response"

    res = Settings.llm.predict_and_call([tool], prompt, verbose = True)
  
    return res.response