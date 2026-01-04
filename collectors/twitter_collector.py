import tweepy
from config import Config

class TwitterCollector:
    def __init__(self):
        self.client = None
        self.setup_client()

    def setup_client(self):
        try:
            self.client = tweepy.Client(
                bearer_token=Config.TWITTER_BEARER_TOKEN,
                consumer_key=Config.TWITTER_API_KEY,
                consumer_secret=Config.TWITTER_API_SECRET,
                access_token=Config.TWITTER_ACCESS_TOKEN,
                access_token_secret=Config.TWITTER_ACCESS_SECRET
            )
        except Exception as e:
            print("Twitter setup error:", e)

    def search_tweets(self, query, max_results=10):
        if not self.client:
            return []

        try:
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=["created_at", "author_id", "geo", "public_metrics"],
                expansions=["author_id"],
                user_fields=["username","name"]
            )

            results = []
            if tweets.data:
                users = {u.id: u for u in tweets.includes.get("users", [])}

                for tweet in tweets.data:
                    author = users.get(tweet.author_id)

                    results.append({
                        "source": "Twitter",
                        "content": tweet.text,
                        "author": author.username if author else "Unknown",
                        "url": f"https://twitter.com/user/status/{tweet.id}",
                        "timestamp": tweet.created_at,
                        "metrics": tweet.public_metrics
                    })

            return results

        except Exception as e:
            print("Twitter search error:", e)
            return []
