from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.tools import Tool

def create_analysis_tool():

    def analyze_disaster(text):
        llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

        prompt = f"""
Analyze this disaster report and extract:
- Disaster type
- Location
- Severity
- Key details

Text: {text}
Respond in JSON.
"""

        return llm.invoke([HumanMessage(content=prompt)]).content

    return Tool(
        name="AnalyzeDisaster",
        func=analyze_disaster,
        description="Extract disaster details from text."
    )
