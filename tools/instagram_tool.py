from langchain.tools import Tool
from collectors.instagram_collector import InstagramCollector

def create_instagram_tool():
    collector = InstagramCollector()

    def search_instagram(hashtag):
        results = collector.search_hashtag(hashtag, max_results=15)

        if not results:
            return "No Instagram results found."

        summary = f"Found {len(results)} Instagram posts:\n\n"

        for i, p in enumerate(results[:5], 1):
            summary += f"{i}. @{p['author']}: {p['content'][:200]}...\n"
            summary += f"   Likes: {p['likes']}, URL: {p['url']}\n\n"

        return summary

    return Tool(
        name="SearchInstagram",
        func=search_instagram,
        description="Search Instagram posts by hashtag."
    )
