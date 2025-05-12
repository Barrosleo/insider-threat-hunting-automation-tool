from data_aggregator import generate_simulated_logs
from correlation_engine import correlate_events
from playbook_executor import execute_playbook
from notification_system import send_notifications
from report_generator import generate_report
import os

def main():
    # Ensure required directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    
    # Step 1: Generate or update simulated logs and save to CSV
    logs_df = generate_simulated_logs(200)
    logs_df.to_csv("data/simulated_logs.csv", index=False)
    print("Simulated logs generated and saved.")
    
    # Step 2: Correlate multiple data sources to detect suspicious event patterns
    correlated_events = correlate_events(logs_df)
    print("Data correlation complete. Suspicious events identified:", len(correlated_events))
    
    # Step 3: Execute automated playbook actions based on correlation results
    response_actions = execute_playbook(correlated_events)
    print("Automated playbook executed. Actions taken:", response_actions)
    
    # Step 4: Send notifications for high-risk events
    notifications = send_notifications(correlated_events)
    print("Notifications sent:", notifications)
    
    # Step 5: Generate incident report
    report = generate_report(correlated_events, response_actions, notifications)
    with open("docs/incident_report.json", "w") as f:
        f.write(report)
    print("Incident report generated and saved in docs/incident_report.json")
    
if __name__ == '__main__':
    main()
