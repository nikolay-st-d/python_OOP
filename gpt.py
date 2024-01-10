from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())
client = OpenAI()
def chat_completion(prompt) ->:
    response = client.chat.cpmpletion.create(
        messages=[
            {
            "role": "user",
                "content": prompt,
            }
        ],
        model = "gpt-3.5-turbo-1106",
    )
    return response.choices[0].message.content

chat_completion("what is 1+1?")