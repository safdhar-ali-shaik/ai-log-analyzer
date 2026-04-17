import random
import time

logs = [
    "INFO: Service started successfully",
    "INFO: Connected to database",
    "INFO: Request processed successfully",
    "WARNING: High memory usage detected",
    "WARNING: Disk space running low",
    "ERROR: Failed to connect to database",
    "ERROR: Timeout while calling API",
    "ERROR: Service unavailable",
]

def generate_logs():
    with open("logs.txt", "w") as f:
        for _ in range(10):
            log = random.choice(logs)
            f.write(log + "\n")
            time.sleep(0.1)

    print("✅ Logs generated in logs.txt")

if __name__ == "__main__":
    generate_logs()
