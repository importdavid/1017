from email import message
import smtplib
import sys
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# For gmail smtp authentication
EMAIL = "wilkidav@gmail.com"
PASSWORD = "vmuhuobietslsuwt"

# for a more complete list of carrier sms and mms gateways
# https://20somethingfinance.com/how-to-send-text-messages-sms-via-email-for-free/
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtex.com",
    "sprint": "@page.nextel.com",
    "fi": "@msg.fi.google.com"
}

def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]

    msg = MIMEMultipart()
    #msg['Subject'] = 'What should the subject be?'
    msg['From'] = EMAIL
    msg['To'] = recipient

    msg.attach(MIMEText(message))
    # msg.attach(MIMEText('<html><body><h1>Hello World</h1>', 'html', 'utf-8'))
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.ehlo()
    server.login(EMAIL, PASSWORD)
    
    server.sendmail(EMAIL, recipient, msg.as_string())
    server.quit()

def main():
    if len(sys.argv) < 4:
        print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
        sys.exit(0)
 
    phone_number = sys.argv[1]
    carrier = sys.argv[2]
    message = sys.argv[3]

    #send_message(phone_number, carrier, message)

if __name__ == "__main__":
    main()