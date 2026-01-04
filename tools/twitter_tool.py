from langchain.tools import Tool
from collectors.twitter_collector import TwitterCollector

def create_twitter_tool():
    collector = TwitterCollector()

    def search_twitter(query):
        results = collector.search_tweets(query, max_results=20)

        if not results:
            return "No Twitter results found."

        summary = f"Found {len(results)} tweets:\n\n"

        for i, t in enumerate(results[:5], 1):
            summary += f"{i}. @{t['author']}: {t['content'][:200]}...\n"
            summary += f"   URL: {t['url']}\n\n"

        return summary

    return Tool(
        name="SearchTwitter",
        func=search_twitter,
        description="Search recent tweets about disasters."
    )
