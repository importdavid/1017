import smtplib, sys, os, random
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import openai
from create_prompt import create_prompt
from gpt3 import gpt3

# For gmail smtp authentication
EMAIL = "wilkidav@gmail.com"
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

# RECIPIENT = "2487901659@msg.fi.google.com"
RECIPIENT = "wilkidav@gmail.com" # For testing

# Atlas image repo
IMAGES = '/home/blondbeard/projects/1017/atlas_images'

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
    return response.choices[0].text


def main(testing=False):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = RECIPIENT

    # Pick a random image from the Atlas repo
    filename = random.choice(os.listdir(IMAGES))
    path = f'{IMAGES}/{filename}'

    with open(path, 'rb') as f:
        img_data = f.read()
        image = MIMEImage(img_data, name=os.path.basename(path))
        msg.attach(image)

    # generate poem with gpt3
    prompt = create_prompt()
    poem = gpt3(prompt).lstrip()
    print(poem)
    msg.attach(MIMEText(poem))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.ehlo()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, RECIPIENT, msg.as_string())
    server.quit()

    # # Debug tracing for msg size concerns
    # print(sys.getsizeof(msg.as_string().encode('utf-8')))
    # print(sys.getsizeof(image.as_bytes()))
    # print(server.esmtp_features['size'])
    

if __name__ == "__main__":
    main()