from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

messages = []

while True:
    user_input = input("👨🏻‍🎓 ")

    if user_input.lower() == 'exit':
        break

    messages.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=messages
    )

    messages.append({"role": "assistant", "content": response.output_text})
    print("🤖 > ", response.output_text)