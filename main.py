import os
import openai



api_key = os.environ.get('PYTHON_API_KEY')
# print(api_key)
openai.api_key = api_key
# client = OpenAI()

def chat_with_sui(prompt):
    res = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return res


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        response =chat_with_sui(user_input)
        print("Chatbot: ", response)