from flask import Flask,request
from main import chat_with_sui


app = Flask(__name__)

@app.route('/',methods =["POST"])
def home():
    if request.is_json:
        data = request.get_json()
        message = data.get('message')
        return f'{message}'
    else:
     return 'Invalid request format. Please send JSON data.'
    # return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'