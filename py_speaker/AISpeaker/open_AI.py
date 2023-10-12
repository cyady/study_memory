import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = ""


"""messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]"""


messages = []
while True:
    user_content = input("user : ")
    messages.append({"role" : "user", "content" : f"{user_content}"})

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    # , messages=[
    #     {"role": "user", "content": "Hello!"}   #역할을 user로 Hello라는 컨텐츠를 보낸것
    #     ])

    assistant_content = chat_completion.choices[0].message.content.strip()

    messages.append({"role" : "assistant", "content" : f"{assistant_content}"})

    print(f"GPT : {assistant_content}")   #지피티 한테 받은 대답