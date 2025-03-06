from flask import Flask
from flask import request
from model import *

import nest_asyncio
import asyncio

nest_asyncio.apply()

app = Flask(__name__)

@app.route('/api/next_card_play', methods=['POST'])
def next_card():
    
    next_card = predict_next_card(request.json)
    
    return next_card

async def main():
    if __name__ == '__main__':
        init_llm()
        
        app.run(host='0.0.0.0', port=9000, debug=True)

asyncio.run(main())