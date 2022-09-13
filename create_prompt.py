from random import random, randint, choice, sample
from datetime import datetime
from AP import AP

def create_prompt():
    prompt = ""
    for i in range(9):
        prompt += choice(AP['blocks'])
    prompt += "\nWrite an epic fantasy sonnet summarizing the above adventures of Atlas."
    # prompt += "\nWrite 2 different haikus summarizing the above adventures of Atlas."

    print(prompt)
    return prompt

if __name__ == "__main__":
    create_prompt()