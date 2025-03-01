from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.core.tools import FunctionTool
from llama_index.core import PromptTemplate

from country_tool import *
from article_service import *
from link_tool import *

llm_model_name = "llama3.1"

def init_llm(): 
    Settings.llm = Ollama(model=llm_model_name, request_timeout=1000.0, base_url = "http://ollama-docker:11434", temperature=0) #, context_window=22000

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