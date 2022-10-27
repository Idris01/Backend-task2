from flask import Flask, jsonify
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)
DEBUG = False if os.getenv('DEBUG', "False")\
            == "False" else True
app.config['DEBUG'] = DEBUG


@app.route('/', methods=['GET'])
def home():
    data = dict(
            slackUsername="Idris Adebowale",
            backend=True,
            age=31,
            bio="Data Scientist and Associate Cloud Engineer")
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
