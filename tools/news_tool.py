from langchain.tools import Tool
from collectors.news_collector import NewsAPICollector

def create_news_tool():
    collector = NewsAPICollector()

    def search_news(query):
        results = collector.search_news(query)

        summary = "Found news articles:\n\n"

        for i, a in enumerate(results[:5], 1):
            summary += f"{i}. {a['content'][:200]}...\n"
            summary += f"   Source: {a['author']}, URL: {a['url']}\n\n"

        return summary

    return Tool(
        name="SearchNews",
        func=search_news,
        description="Search disaster-related news."
    )
