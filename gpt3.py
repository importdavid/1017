import openai
import os

openai.api_key = os.getenv("OPEN_AI_API_KEY")
openai.organization = os.getenv("OPEN_AI_ORGANIZATION")

def gpt3(prompt, engine='text-davinci-002'):
    ENGINES = ['text-ada-001', 'text-babbage-001', 'text-curie-001', 'text-davinci-002']
    if type(engine) == int:
        engine = ENGINES[engine]

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=0.1,
        max_tokens=128,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # content = response.choices[0].text.split('.')
    # print(content)
    return response.choices[0].text