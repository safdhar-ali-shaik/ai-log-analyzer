from analyzer.log_watcher import follow
from analyzer.basic_analyzer import analyze_log

log_file = "/datalex/node-express-boilerplate/logs/app.log"

for log in follow(log_file):
    result = analyze_log(log)
    print("AI OUTPUT:", result)
