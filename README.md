# íº€ AI Log Analyzer (DevOps + AI Project)

## í³Œ Overview

AI Log Analyzer is a real-time log processing system that ingests application logs, analyzes them using rule-based and AI techniques, and provides actionable insights.

This project simulates a **production-like DevOps pipeline**:

* Application â†’ Logs â†’ Analyzer â†’ Insights

---

## í·± Architecture

```
Node.js App (Express)
        â†“
Winston Logger
        â†“
Log Files (app.log / error.log)
        â†“
Python Log Watcher (tail -f style)
        â†“
AI Analyzer
        â†“
Insights / Alerts
```

---

## âš™ï¸ Tech Stack

* **Backend App:** Node.js (Express)
* **Database:** MongoDB (Docker)
* **Logging:** Winston
* **Analyzer:** Python
* **Future:** FastAPI, Grafana, AWS (Terraform)

---

## í³ Project Structure

```
ai-log-analyzer/
â”œâ”€â”€ analyzer/
â”‚   â”œâ”€â”€ basic_analyzer.py
â”‚   â”œâ”€â”€ log_watcher.py
â”‚   â””â”€â”€ run_pipeline.py
â”œâ”€â”€ ingestion/
â”œâ”€â”€ api/
â”œâ”€â”€ ui/
â”œâ”€â”€ docker/
â”œâ”€â”€ infra/
â”œâ”€â”€ data/
â”œâ”€â”€ tests/
â””â”€â”€ README.md
```

---

## íº€ Setup Instructions

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

## í´– Run AI Log Analyzer

In a new terminal:

```bash
python analyzer/run_pipeline.py
```

---

## í³Š Example Output

```
AI OUTPUT: {'level': 'high', 'message': 'error: GET /v1/users 401'}
AI OUTPUT: {'level': 'low', 'message': 'info: GET /v1/docs 200'}
```

---

## í´¥ Features (Current)

* âœ… Real-time log ingestion
* âœ… File-based logging (Winston)
* âœ… Rule-based log analysis
* âœ… Streaming log pipeline (tail -f style)

---

## íº§ Roadmap

* [ ] Anomaly detection (ML models)
* [ ] REST API (FastAPI)
* [ ] Dashboard UI
* [ ] Grafana integration
* [ ] Dockerization
* [ ] AWS deployment (Terraform)

---

## í·  DevOps Concepts Covered

* Log ingestion pipelines
* Observability basics
* Microservice logging patterns
* Real-time stream processing
* Infrastructure-ready design

---

## í³Œ Author

**Safdhar Ali Shaik**

---

## â­ Goal

Build a **production-ready AI-powered log analysis system** demonstrating real-world DevOps and observability.


