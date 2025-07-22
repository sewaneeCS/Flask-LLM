
from openai import OpenAI #type: ignore
client = OpenAI(
    api_key = 'SECRET_KEY'
)


def prompt(text):
    completion = client.responses.create(
        model="gpt-4.1-mini",
        input=text
    )
    answer = completion.output_text
    return answer
