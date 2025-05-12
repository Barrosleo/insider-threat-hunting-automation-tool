import pandas as pd
import random
import datetime

def generate_simulated_logs(num_records=100):
    # Define possible sources and activity types
    sources = ['login', 'file', 'network']
    users = ['alice', 'bob', 'charlie', 'dave']
    activities = {
        'login': ['login-success', 'login-failure'],
        'file': ['file-read', 'file-write'],
        'network': ['download', 'upload']
    }
    details = {
        'login': ['normal', 'invalid credentials'],
        'file': ['document1.pdf', 'confidential_report.pdf', 'sensitive_data.docx'],
        'network': ['small_file.zip', 'large_file.zip']
    }
    
    logs = []
    for i in range(num_records):
        src = random.choice(sources)
        log = {
            "event_id": i+1,
            "timestamp": datetime.datetime.now().isoformat(),
            "source": src,
            "user": random.choice(users),
            "activity": random.choice(activities[src]),
            "detail": random.choice(details[src])
        }
        logs.append(log)
    return pd.DataFrame(logs)

if __name__ == '__main__':
    df = generate_simulated_logs(10)
    print(df.head())
