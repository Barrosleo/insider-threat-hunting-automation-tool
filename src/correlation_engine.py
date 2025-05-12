def correlate_events(df):
    """
    Applies correlation rules to identify suspicious sequences:
    - For example, a 'login-failure' followed by a 'file-read' or 'file-write' from the same user within a short time.
    - This function flags events as suspicious by adding a new column 'suspicious' with True/False.
    """
    df["suspicious"] = False
    df["correlation_reason"] = ""
    
    # Simple rule: if a login-failure is immediately followed by any file-related action by the same user, flag it.
    # Loop over rows and look for patterns (this is a simplified example)
    for idx in range(len(df) - 1):
        current = df.iloc[idx]
        next_event = df.iloc[idx + 1]
        if (current["source"] == "login" and current["activity"] == "login-failure" and
            next_event["source"] == "file" and current["user"] == next_event["user"]):
            df.at[df.index[idx + 1], "suspicious"] = True
            df.at[df.index[idx + 1], "correlation_reason"] = "file activity following login failure"
    # Return only suspicious events for further processing
    suspicious_events = df[df["suspicious"] == True]
    return suspicious_events

if __name__ == '__main__':
    import pandas as pd
    from data_aggregator import generate_simulated_logs
    df_sample = generate_simulated_logs(20)
    suspicious = correlate_events(df_sample)
    print(suspicious)
