from database import init_database
from agent import DisasterMonitoringAgent
from monitor import MonitorRunner

def main():
    print("Initializing Disaster Monitoring Agent...")

    init_database()

    agent = DisasterMonitoringAgent()
    monitor = MonitorRunner(agent)

    print("\n--- General Monitoring ---\n")
    print(monitor.run_default())

    print("\n--- Hurricanes ---\n")
    print(agent.monitor_disasters("Search for recent hurricane alerts"))

    print("\n--- Pacific Tsunami Alerts ---\n")
    print(agent.monitor_disasters("Find tsunami warnings in Pacific region"))

if __name__ == "__main__":
    main()
