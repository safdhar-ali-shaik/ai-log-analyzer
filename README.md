# 🚀 AI Log Analyzer (DevOps + AI Project)

## 📌 Overview

AI Log Analyzer is a real-time log processing system that ingests application logs, analyzes them using rule-based and AI techniques, and provides actionable insights.

This project simulates a **production-like DevOps pipeline**:

* Application → Logs → Analyzer → Insights

---

## 🧱 Architecture

```
Node.js App (Express)
        ↓
Winston Logger
        ↓
Log Files (app.log / error.log)
        ↓
Python Log Watcher (tail -f style)
        ↓
AI Analyzer
        ↓
Insights / Alerts
```

---

## ⚙️ Tech Stack

* **Backend App:** Node.js (Express)
* **Database:** MongoDB (Docker)
* **Logging:** Winston
* **Analyzer:** Python
* **Future:** FastAPI, Grafana, AWS (Terraform)

---

## 📁 Project Structure

```
ai-log-analyzer/
├── analyzer/
│   ├── basic_analyzer.py
│   ├── log_watcher.py
│   └── run_pipeline.py
├── ingestion/
├── api/
├── ui/
├── docker/
├── infra/
├── data/
├── tests/
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/safdhar-ali-shaik/ai-log-analyzer.git
cd ai-log-analyzer
```

---

### 2. Run Sample Application (Log Generator)

Clone and run:

```bash
git clone https://github.com/hagopj13/node-express-boilerplate.git
cd node-express-boilerplate
```

---

### 3. Setup environment

Create `.env`:

```env
PORT=3000
MONGODB_URL=mongodb://localhost:27017/dev-db
JWT_SECRET=supersecret
```

---

### 4. Run MongoDB

```bash
docker run -d -p 27017:27017 --name mongodb mongo:6
```

---

### 5. Enable file logging

Update Winston logger to write logs to:

```
logs/app.log
logs/error.log
```

---

### 6. Start the application

```bash
npm install
npm run dev
```

---

### 7. Generate logs

```bash
curl http://localhost:3000/v1/users
curl http://localhost:3000/v1/unknown
```

---

## 🤖 Run AI Log Analyzer

In a new terminal:

```bash
python analyzer/run_pipeline.py
```

---

## 📊 Example Output

```
AI OUTPUT: {'level': 'high', 'message': 'error: GET /v1/users 401'}
AI OUTPUT: {'level': 'low', 'message': 'info: GET /v1/docs 200'}
```

---

## 🔥 Features (Current)

* ✅ Real-time log ingestion
* ✅ File-based logging (Winston)
* ✅ Rule-based log analysis
* ✅ Streaming log pipeline (tail -f style)

---

## 🚧 Roadmap

* [ ] Anomaly detection (ML models)
* [ ] REST API (FastAPI)
* [ ] Dashboard UI
* [ ] Grafana integration
* [ ] Dockerization
* [ ] AWS deployment (Terraform)

---

## 🧠 DevOps Concepts Covered

* Log ingestion pipelines
* Observability basics
* Microservice logging patterns
* Real-time stream processing
* Infrastructure-ready design

---

## 📌 Author

**Safdhar Ali Shaik**

---

## ⭐ Goal

Build a **production-ready AI-powered log analysis system** demonstrating real-world DevOps and observability.


