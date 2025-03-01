import aiohttp
import asyncio

from pydantic import Field
from bs4 import BeautifulSoup

async def make_http_request(urls: list[str] = Field(description="a list of links found in the content"), original_promt = Field(description="The original full prompt")):
    """Usfeful for extracting one or more links from a prompt"""

    async with aiohttp.ClientSession() as session:
        async with aiohttp.ClientSession() as session:
            tasks = [fetch(url, session) for url in urls]
        
            results = await asyncio.gather(*tasks)

            rag_content = ' '.join(results)

            return f"{original_promt} Rely only on the following content when generating a response: {rag_content}"
        
async def fetch(url, session):
    """Asynchronous function to fetch a URL"""
    
    async with session.get(url) as response:
        text = await response.text()
       
        soup = BeautifulSoup(text, "html.parser")
        paragraphs = soup.find_all("p")
            
        article_text = ' '.join([p.get_text() for p in paragraphs])

        return f"The content from {url} is {article_text}"