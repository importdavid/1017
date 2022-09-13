import os

x = "GMAIL_APP_PASSWORD"
y = "OPEN_AI_API_KEY"
z = "OPEN_AI_ORGANIZATION"

for w in [x,y,z]: print(f"{w}: {os.getenv(w)}")