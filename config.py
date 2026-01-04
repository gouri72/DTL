import os

class Config:
    # Twitter API
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
    TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

    # Instagram
    INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    DISASTER_KEYWORDS = [
        "tsunami","flood","flooding","hurricane",
        "cyclone","storm surge","high tide",
        "tidal wave","emergency evacuation"
    ]

    DB_NAME = "disaster_news.db"
