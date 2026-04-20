from analyzer.log_watcher import follow
from analyzer.basic_analyzer import analyze_log

log_file = "/projects/node-express-boilerplate/logs/app.log"

print("🚀 Starting AI Log Analyzer...")

for log in follow(log_file):
    result = analyze_log(log)

    # Only print meaningful logs
    if result["severity"] != "LOW":
        print("⚠️ ALERT:", result)
    else:
        print("ℹ️ INFO:", result["type"])