import tweepy
import openai

class SocialMediaBot:
    def __init__(self):
        self.api_key = "YOUR_TWITTER_API_KEY"
        self.openai_key = "YOUR_OPENAI_KEY"

    def post_daily_update(self):
        businesses = self.fetch_new_listings()
        for biz in businesses:
            tweet = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Create a tweet for {biz['name']}"}]
            )
            tweepy.Client(self.api_key).create_tweet(text=tweet)

if __name__ == "__main__":
    bot = SocialMediaBot()
    bot.post_daily_update()
