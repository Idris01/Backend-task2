from flask import Flask, jsonify,request
import os
from dotenv import load_dotenv
from flask_cors import CORS
from utility import operands, calculate
    
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
        
        answer = ...
        
        if len(operation.strip()) == 1:
            for item,options in operands.items():
                if operation == options[0]:
                    answer = calculate(x,y,operation)
                    break
        else:
            for items in operands.values():
                items = list(items)
                if str(operation[:3]).lower() in ''.join(items):
                    answer = calculate(x,y,items[0])
                    break
        result=dict(
                slackUsername="Idris Adebowale",
                result=int(answer),
                operation_type=data['operation_type']
                )
        return jsonify(result)
                    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
