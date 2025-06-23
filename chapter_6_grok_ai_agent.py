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
    response = genai.generate_text(
        model="gemini-pro",
        prompt=f"Write an engaging Twitter post about: {topic}",
    )
    return response.text


tweet = generate_tweet("AI in 2024")
print(tweet)


## Auto-Post Tweets ##
def post_tweet(content):
    twitter_api.update_status(content)
    print("Tweet posted!")


post_tweet("AI is changing the world. Are you ready?")
