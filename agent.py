from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from tools.twitter_tool import create_twitter_tool
from tools.instagram_tool import create_instagram_tool
from tools.news_tool import create_news_tool
from tools.analysis_tool import create_analysis_tool
from config import Config

class DisasterMonitoringAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0,
            model="gpt-4o-mini",
        )

        self.tools = [
            create_twitter_tool(),
            create_instagram_tool(),
            create_news_tool(),
            create_analysis_tool()
        ]

        self.agent = self._create_agent()

    def _create_agent(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", """
You are a disaster monitoring AI agent.
Collect & cross-verify reports from Twitter, Instagram, and news sources.
Focus on tsunamis, floods, cyclones, storm surges, and emergency alerts.
"""),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad")
        ])

        agent = create_openai_tools_agent(self.llm, self.tools, prompt)

        return AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True
        )

    def monitor_disasters(self, query):
        result = self.agent.invoke({"input": query})
        return result["output"]
