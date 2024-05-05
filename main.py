import os
from openai import OpenAI
import openai



api_key = os.environ.get('PYTHON_API_KEY2')
print(api_key)
openai.api_key = api_key

def chat_with_sui(prompt):
    res = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role":"user","content":prompt}],
        # stream=True
    )
    return res


# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit","exit","bye"]:
#             break
#         response =chat_with_sui(user_input)
#         print("Chatbot: ", response)

mess = "getting this error when i try to build or test my sui move package with my wsl2 ubuntu powershell Failed to resolve dependencies for package 'quest-solution' Caused by: 0: Parsing manifest for 'sui' 1: No such file or directory (os error 2)"

print(chat_with_sui(mess))