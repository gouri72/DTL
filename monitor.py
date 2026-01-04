class MonitorRunner:
    def __init__(self, agent):
        self.agent = agent

    def run_default(self):
        query = """
Monitor disasters including:
- tsunamis
- floods
- hurricanes
- abnormal tides
- evacuation alerts

Summarize critical findings.
"""
        return self.agent.monitor_disasters(query)
