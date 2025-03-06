from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.core.tools import FunctionTool
from llama_index.core import PromptTemplate

from card_tool import *
from article_service import *
from link_tool import *

llm_model_name = "llama3.1"
 
def init_llm(): 
    Settings.llm = Ollama(model=llm_model_name, request_timeout=1000.0, base_url = "http://ollama-docker:11434", temperature=0) #, context_window=22000

def predict_next_card(cards: list[int]):
    current_number = cards.pop(0)

    print(cards) 

    play_without_special_cards = filter(lambda p: p > 0 and p != 2 and p != 10, cards)
    special_cards = filter(lambda p: p == 2 or p == 10, cards)

    tool1 = FunctionTool.from_defaults(fn=get_lowest_next_number, name="select_the_lowest_number_that_is_greater_than_the_current_number", return_direct=True)
    tool2 = FunctionTool.from_defaults(fn=get_two_or_ten, name="get_two_or_ten", return_direct=True)
    
    prompt = f"""The play list contains {list(play_without_special_cards)}. The current play is {current_number}"""
    res = Settings.llm.predict_and_call([tool1], prompt, verbose = True)

    print(f"current card: {current_number}")

    result = res.response

    if int(result) == 0:
        print("checking specal cards")
        prompt = f"""The play list contains {list(special_cards)}. The current play is {current_number}"""
        res2 = Settings.llm.predict_and_call([tool2], prompt, verbose = True)
        result = res2.response
    
    print(f"Just played {result}")
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