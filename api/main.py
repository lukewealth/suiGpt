import os
from openai import OpenAI
import openai



api_key = os.environ.get('PYTHON_API_KEY')
# print(api_key)
client = OpenAI()
openai.api_key = api_key

def chat_with_sui(prompt):
    res = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        stream=True
    )
    return res

# res = chat_with_sui("In 30 words summarize the flask app")
# for chunk in res:
#     if chunk.choices[0].delta.content is not None:
#         print((chunk.choices[0].delta.content))


# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit","exit","bye"]:
#             break
#         response =chat_with_sui(user_input)
#         print("Chatbot: ", response)