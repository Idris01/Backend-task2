from flask import Flask, jsonify,request
import os
import re
from dotenv import load_dotenv
from flask_cors import CORS
from utility import operands, calculate, response
    
load_dotenv()

app = Flask(__name__)
CORS(app)

DEBUG = False

if os.getenv('DEBUG','False') == 'True':
    DEBUG = True

app.config['DEBUG'] = DEBUG

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        data = dict(
            slackUsername="Idris Adebowale",
            backend=True,
            age=31,
            bio="Hi, I am a pationate Data Scientist and Associate Cloud Engineer")
        return jsonify(data)
    
    else:
        data = request.get_json()
        operation = data['operation_type']
        x = float(data['x'])
        y = float(data['y'])
        
        answer = None
        operation_type = None

        if len(operation.strip()) == 1:
            for item,options in operands.items():
                if operation == options[0]:
                    answer = calculate(x,y,operation)
                    operation_type = item
                    break
        elif len(operation.strip().split()) == 1:
            for name, items in operands.items():
                items = list(items)
                if str(operation[:3]).lower() in ''.join(items):
                    answer = calculate(x,y,items[0])
                    operation_type = name
                    break
        else:
            bot_response = response(operation).choices[0].text
            pattern = '\d+,?\d+'
            try:
                answer = re.findall(pattern,bot_response)
                if answer:
                    answer = int(answer[-1].replace(',',''))
                    for name, items in operands.items():
                        items = list(items)[1:]
                        for item in items:
                            if item.lower()[:3] in bot_response.lower():
                                operation_type = name
                                break
                        if operation_type:
                            break
                else:
                    answer = 0
                    operation_type = 'Unknown'
            except TypeError:
                operation_type='error'
                answer = 0

        result=dict(
                slackUsername="Idris Adebowale",
                result=int(answer),
                operation_type=operation_type
                )
        return jsonify(result)
                    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
