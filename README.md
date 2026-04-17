# 🚀 AI Log Analyzer (DevOps + AI)

This project simulates a real-world DevOps workflow by generating system logs and analyzing them using a local AI model.

---

## 🎯 What This Project Does

* Generates realistic system logs
* Uses a local AI model to analyze logs
* Provides:

  * Error summary
  * Root cause
  * Suggested fixes

---

## 🛠️ Tech Stack

* Python
* Ollama (Local LLM - phi3)
* DevOps concepts (log analysis, automation)

---

## 📂 Project Structure

```
ai-log-analyzer/
├── app.py              # AI log analyzer
├── log_generator.py    # Generates logs
├── logs.txt            # Generated logs
```

---

## ▶️ How to Run

### 1. Start Ollama

```
ollama run phi3
```

---

### 2. Generate Logs

```
python log_generator.py
```

---

### 3. Analyze Logs

```
python app.py
```

---

## 🧠 How It Works

1. Log generator simulates application/system logs
2. Logs are stored in `logs.txt`
3. AI model analyzes logs and returns:

   * Issues detected
   * Possible causes
   * Fix recommendations

---

## 💡 Use Case

In real DevOps environments, engineers analyze logs to troubleshoot failures.
This project automates that process using AI.

---

## 📌 Future Improvements

* CLI support (analyze any log file)
* Docker containerization
* Jenkins pipeline integration
* AWS ECS deployment

---

