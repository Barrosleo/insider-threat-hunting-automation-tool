# insider threat hunting automation tool

this project simulates an automated insider threat hunting system that aggregates simulated log data (login records, file access logs, network traffic), correlates events to detect suspicious insider behavior, executes automated playbook actions (e.g., isolating a user account), sends notifications via a simulated messaging system, and generates detailed incident reports.

## key features
- **data correlation:** integrates diverse logs to identify abnormal event patterns.
- **automated playbooks:** triggers response actions when insider threats are detected.
- **notification system:** simulates sending high-fidelity alerts.
- **incident reporting:** produces detailed reports with recommendations.
- **on-call extensibility:** supports periodic health checks or real-time alerts (optional).

## usage
1. Install dependencies:

pip install -r requirements.txt

3. Run the main application:

python src/main.py


## repository structure
insider-threat-hunting-automation-tool/
├── README.md
├── requirements.txt
├── docs/
│   └── incident_report.json
├── data/
│   └── simulated_logs.csv
└── src/
    ├── main.py
    ├── data_aggregator.py
    ├── correlation_engine.py
    ├── playbook_executor.py
    ├── notification_system.py
    └── report_generator.py

