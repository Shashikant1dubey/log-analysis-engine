# 🧠 Log Analysis Engine (Python)

## 📌 Overview

The **Log Analysis Engine** is a lightweight, modular Python project that processes system logs, categorizes events, and detects anomalies such as elevated error rates.

It demonstrates a **production-style architecture** using CLI execution, modular design, and pipeline-based processing.

---

## 🚀 Key Features

- 🖥️ CLI-based execution
- 🧩 Modular architecture (`core`, `pipelines`)
- 📄 Log parsing and categorization (INFO, WARNING, ERROR)
- 🚨 Basic anomaly detection (error threshold alert)
- 🔁 Pipeline-based processing flow
- 📦 Clean and scalable project structure

---

## 🏗️ Project Structure
log-analysis-engine/
│
├── src/
│ ├── core/
│ │ └── processor.py
│ │
│ ├── pipelines/
│ │ └── run_pipeline.py
│ │
│ └── main.py
│
├── data/
│ └── sample_logs.txt
│
├── tests/
│ └── test_processor.py
│
├── logs/
├── requirements.txt
└── README.md

---

## ⚙️ How It Works

1. Reads logs from `data/sample_logs.txt`
2. Processes each log line
3. Categorizes logs into:
   - INFO
   - WARNING
   - ERROR
4. Generates a summary report
5. Triggers an alert if error count exceeds threshold

---

## ▶️ How to Run

Run the project from the root directory:
python3 -m src.main --task log_analysis

🧪 Run Tests
python3 -m pytest

📦 Install Dependencies
pip install -r requirements.txt
Example requirements.txt:
pytest

💡 Example Output
Log Summary:
INFO: 3
WARNING: 1
ERROR: 2
ALERT: High number of errors detected!

🧠 Skills Demonstrated
Python modular architecture
CLI application design
Pipeline-based system design
Basic log monitoring and anomaly detection
Proper package structure and imports

🚀 Future Improvements
Real-time log streaming (Kafka / file watcher)
FastAPI backend for log analysis
Docker containerization
Database storage (PostgreSQL / MongoDB)
Dashboard visualization (Streamlit / React)
