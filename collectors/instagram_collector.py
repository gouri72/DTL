from instagrapi import Client
from config import Config

class InstagramCollector:
    def __init__(self):
        self.client = None
        self.setup_client()

    def setup_client(self):
        try:
            self.client = Client()
            self.client.login(Config.INSTAGRAM_USERNAME, Config.INSTAGRAM_PASSWORD)
        except Exception as e:
            print("Instagram setup error:", e)

    def search_hashtag(self, hashtag, max_results=10):
        if not self.client:
            return []

        hashtag = hashtag.replace("#", "")

        try:
            medias = self.client.hashtag_medias_recent(hashtag, amount=max_results)

            return [
                {
                    "source": "Instagram",
                    "content": m.caption_text or "",
                    "author": m.user.username,
                    "url": f"https://instagram.com/p/{m.code}",
                    "timestamp": m.taken_at,
                    "likes": m.like_count
                }
                for m in medias
            ]

        except Exception as e:
            print("Instagram search error:", e)
            return []
