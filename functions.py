
from openai import OpenAI #type: ignore
client = OpenAI(
    api_key = 'SECRET_KEY'
)
mdl = "gpt-4.1-mini"


def prompt(text):
    completion = client.responses.create(
        model=mdl,
        input=text
    )
    answer = completion.output_text
    return answer

def getmodel():
    return mdl
