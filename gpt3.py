import openai
import os

openai.api_key = os.getenv("OPEN_AI_API_KEY")
openai.organization = os.getenv("OPEN_AI_ORGANIZATION")

def gpt3(stext):
    response = openai.Completion.create(
        engine = 'text-ada-001',
        prompt = stext,
        
        temperature = 0.1,
        max_tokens = 64,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )

    # content = response.choices[0].text.split('.')
    # print(content)
    return response.choices[0].text