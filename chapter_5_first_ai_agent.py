import openai
import os
from dotenv import load_dotenv
# Load API Key

# This assumes that you have the `OPENAI_API_KEY` in a `.env` file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def email_assistant(email_content):
    response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI Email Assistant."},
                {"role": "user", "content": f"Summarize this email: {email_content}"},
                ]
            )
    return response['choices'][0]['message']['content']


### EXAMPLE ###
email_text = "Hi John, we’d like to schedule a meeting next Wednesday at 3 PM. Let us know if that works!"
summary = email_assistant(email_text)
print(summary) # Expected output: Meeting request for next Wednesday at 3 PM. Awaiting response.


def suggest_reply(email_content):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI Email Assistant."},
            {"role": "user", "content": f"Suggest a professional reply to this email {email_content}"},
            ]
        )
    return response['choices'][0]['message']['content']


### EXAMPLE ###
reply = suggest_reply(email_text)
print(reply) # Expected output: Hello, thanks for reaching out! Next Wednesday at 3 PM works for me. Looking forward to it.

### CONNECTING THE AI AGENT TO AN EMAIL API ###

# Run: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

from googleapiclient.discovery import build
from google.oauth2 import service_account

# Authenticate Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
service = build('gmail', 'v1', credentials=creds)

# Get email messages
def get_emails():
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])
    for msg in messages:
        email_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        print(email_data['snippet']) # Prints email preview

get_emails()

def auto_reply():
    results = service.users().messages().list(userId='me', maxResults=3).execute()
    messages = results.get('messages', [])
    for msg in messages:
        email_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        email_content = email_data['snippet']
        summary = email_assistant(email_content)
        reply = suggest_reply(email_content)
        print(f"\n Email: {summary}")
        print(f"Suggested Reply: {reply}")

auto_reply()
