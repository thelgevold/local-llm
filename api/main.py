from flask import Flask
from flask import request
from model import *

import nest_asyncio
import asyncio

nest_asyncio.apply()

app = Flask(__name__)

@app.route('/api/country', methods=['POST'])
def post_question():
    country = request.json['country']
    
    response = predict(country)
    
    return response

async def main():
    if __name__ == '__main__':
        init_llm()
        
        app.run(host='0.0.0.0', port=9000, debug=True)

asyncio.run(main())