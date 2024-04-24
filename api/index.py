from flask import Flask,request
from main import chat_with_sui


app = Flask(__name__)

@app.route('/ans',methods =["POST"])
def home():
    def generator():
        if request.is_json:
            data = request.get_json()
            message = data.get('message')
            res = chat_with_sui(message)
            for chunk in res:
                if chunk.choices[0].delta.content is not None:
                    yield(chunk.choices[0].delta.content)
        else:
            return 'Invalid request format. Please send JSON data.'
    return  generator(), {"Content-Type":"text/plain"}

@app.route('/')
def about():
    return 'hello world'