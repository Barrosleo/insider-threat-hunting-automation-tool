def execute_playbook(suspicious_events):
    """
    For each suspicious event, execute an automated playbook action.
    Actions could include isolating the user account and flagging the event.
    Returns a dictionary with event IDs and the actions taken.
    """
    actions_taken = {}
    for idx, event in suspicious_events.iterrows():
        if event["suspicious"]:
            # Example action: if correlation_reason exists and event is high-risk, then isolate the account.
            actions_taken[event["event_id"]] = "isolate user account and escalate to security team"
    return actions_taken

if __name__ == '__main__':
    import pandas as pd
    from correlation_engine import correlate_events
    from data_aggregator import generate_simulated_logs
    df_sample = generate_simulated_logs(20)
    suspicious = correlate_events(df_sample)
    actions = execute_playbook(suspicious)
    print(actions)
