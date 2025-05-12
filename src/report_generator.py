import json
from datetime import datetime

def generate_report(suspicious_events, actions_taken, notifications):
    """
    Generates a JSON report that includes:
      - Total number of suspicious events
      - The playbook actions executed
      - The notifications sent
      - A timestamp for the report generation
    """
    report = {
        "report_generated": datetime.now().isoformat(),
        "suspicious_events_count": len(suspicious_events),
        "actions_taken": actions_taken,
        "notifications": notifications,
        "detailed_events": suspicious_events.to_dict(orient="records")
    }
    return json.dumps(report, indent=4)

if __name__ == '__main__':
    import pandas as pd
    from data_aggregator import generate_simulated_logs
    from correlation_engine import correlate_events
    from playbook_executor import execute_playbook
    from notification_system import send_notifications
    df_sample = generate_simulated_logs(10)
    suspicious = correlate_events(df_sample)
    actions = execute_playbook(suspicious)
    notes = send_notifications(suspicious)
    report = generate_report(suspicious, actions, notes)
    print(report)
