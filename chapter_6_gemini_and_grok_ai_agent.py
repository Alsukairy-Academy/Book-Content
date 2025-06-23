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

## Social Media AI Agent with xAI Grok ##
# Run: pip install tweepy
import tweepy

api_key = "your-twitter-api-key"
api_secret = "your-twitter-api-secret"
access_token = "your-access-token"
access_secret = "your-access-secret"
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
twitter_api = tweepy.API(auth)


##  Fetch Trending Topics ##
def get_trending_topics():
    trends = twitter_api.trends_place(1)  # 1 = Global trends
    return [trend["name"] for trend in trends[0]["trends"][:5]]


print(get_trending_topics())


## Generate AI-Powered Tweets ##
def generate_tweet(topic):
    response = model.generate_text(f"Write an engaging Twitter post about: {topic}")
    return response.text


tweet = generate_tweet("AI in 2024")
print(tweet)


## Auto-Post Tweets ##
def post_tweet(content):
    twitter_api.update_status(content)
    print("Tweet posted!")


post_tweet("AI is changing the world. Are you ready?")
