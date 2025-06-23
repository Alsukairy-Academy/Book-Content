# Run: pip install google-generativeai
import google.generativeai as genai

# Set API Key
genai.configure(api_key="your-api-key-here")
model = genai.GenerativeModel("gemini-2.5-flash")


## Read a Google Doc and Summarize It ##
def summarize_google_doc(doc_text):
    response = model.generate_content(
        f"Summarize this Google Doc content in 3 bullet points:\n{doc_text}"
    )
    return response.text


doc_text = "This is a sample contract detailing terms and conditions..."
summary = summarize_google_doc(doc_text)
print(summary)


## Generate a Professional Email ##
def generate_email(subject, details):
    response = model.generate_content(
        f"Write a professional email with subject '{subject}' and details: {details}"
    )
    return response.text


email = generate_email("Meeting Request", "We need to schedule a meeting next week.")
print(email)

## Automate Calendar Scheduling ##
import datetime


def suggest_meeting_time():
    now = datetime.datetime.now()
    suggested_time = now + datetime.timedelta(days=3, hours=2)
    return f"Suggested Meeting Time: {suggested_time.strftime('%Y-%m-%d %H:%M')}"


print(suggest_meeting_time())
