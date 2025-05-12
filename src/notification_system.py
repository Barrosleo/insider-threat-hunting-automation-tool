def send_notifications(suspicious_events, risk_threshold=0):
    """
    For each suspicious event, simulate sending an alert via a messaging system.
    Here, we assume that if the event is suspicious, a notification is triggered.
    Returns a list of notification messages.
    """
    notifications = []
    for idx, event in suspicious_events.iterrows():
        notification = (f"ALERT: Event {event['event_id']}: User {event['user']} activity flagged "
                        f"({event.get('correlation_reason', 'N/A')}).")
        notifications.append(notification)
    return notifications

if __name__ == '__main__':
    from correlation_engine import correlate_events
    from data_aggregator import generate_simulated_logs
    import pandas as pd
    df_sample = generate_simulated_logs(20)
    suspicious = correlate_events(df_sample)
    notes = send_notifications(suspicious)
    print(notes)
