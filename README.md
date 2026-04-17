# 🧠 Log Analysis Engine (Python)

> Lightweight Observability & Log Intelligence Engine for analyzing system logs, detecting anomalies, and simulating production-grade monitoring pipelines.

---

## 📌 Overview

The **Log Analysis Engine** is a modular Python-based observability tool designed to simulate how modern backend systems process, analyze, and monitor application logs.

It processes log streams, categorizes events, and detects anomaly patterns such as elevated error rates using a **pipeline-driven architecture**.

This project is structured like a real-world backend service with separation of concerns, CLI execution, and extensible components.

---

## 🚀 Key Features

- 🖥️ CLI-driven execution for flexible task handling
- 🧩 Modular architecture (`core`, `pipelines`, `utils`)
- 📄 Log parsing and structured event classification
- 🚨 Rule-based anomaly detection (error threshold alerts)
- 🔁 Pipeline-based processing workflow
- 📦 Clean, scalable, production-style project structure
- 🔧 Easily extensible for real-time or API-based ingestion

---

## 🏗️ System Architecture

```
📦 log-analysis-engine
│
├── 📁 src
│   ├── 📁 core              # Business logic (log parsing & analysis)
│   ├── 📁 pipelines         # Workflow orchestration layer
│   ├── 📁 utils             # Logging & helper utilities
│   └── main.py              # CLI entry point
│
├── 📁 data                  # Sample log datasets
├── 📁 tests                 # Unit tests
├── 📁 logs                  # Runtime logs (ignored in git)
├── 📄 requirements.txt
└── 📄 README.md
```

---

## ⚙️ How It Works

The system follows a simple observability pipeline:

```
Log Source → CLI Input → Pipeline Layer → Core Processing → Output Engine
```

### Processing Flow:
1. Loads logs from `data/sample_logs.txt`
2. Parses each log entry
3. Classifies logs into:
   - INFO
   - WARNING
   - ERROR
4. Generates aggregated summary metrics
5. Triggers alerts if error threshold is exceeded

---

## ▶️ How to Run

### Run Log Analysis

```bash
python3 -m src.main --task log_analysis
```

---

## 🧪 Run Tests

```bash
python3 -m pytest
```

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

### requirements.txt
```
pytest
```

---

## 💡 Example Output

```
Log Summary:
INFO: 3
WARNING: 1
ERROR: 2

ALERT: High number of errors detected!
```

---

## 🧠 Engineering Skills Demonstrated

- Modular system design in Python
- Pipeline-based architecture design
- CLI tool development
- Basic observability system concepts
- Logging and structured processing
- Clean package structuring (`src/ layout`)
- Scalable backend thinking

---

## 🚀 Future Roadmap

This project is designed to evolve into a full observability system:

- 🔄 Real-time log streaming (tail -f / event-driven ingestion)
- ⚡ FastAPI backend for remote log analysis
- 🐳 Docker containerization for deployment
- 📊 Metrics export (Prometheus-style monitoring)
- 🗄️ Persistent storage (PostgreSQL / Elasticsearch)
- 📈 Dashboard UI (Streamlit / React)

---

## 📌 Project Positioning

This project is a **lightweight observability simulation engine**, inspired by real-world monitoring systems used in backend infrastructure (logging, debugging, and system health tracking tools).

---

## 👨‍💻 Author

Built as a systems-style Python project demonstrating backend architecture thinking, modular design, and production-grade code organization principles.
