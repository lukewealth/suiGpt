from flask import Flask,request
from main import chat_with_sui


app = Flask(__name__)

@app.route('/ans', methods=["POST", "GET"])
def home():
    def generator():
        try:
            # data = request.get_json()
            # message = data.get('message')
            res = chat_with_sui("In 30 words summarize the flask app")
            for chunk in res:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            # Handle the exception here (e.g., log the error, return a generic message)
            print(f"An error occurred: {e}")
            yield "An error occurred while processing your request."

    return generator(), {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "http://localhost:3000"}


@app.route('/')
def about():
    return 'hello world'


