import requests

def analyze_logs(log_text):
    url = "http://localhost:11434/api/generate"

    prompt = f"""
    You are a DevOps engineer.

    Analyze the logs and provide:
    1. Error summary
    2. Root cause
    3. Suggested fix

    Logs:
    {log_text}
    """

    data = {
        "model": "phi3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    return response.json()["response"]


if __name__ == "__main__":
    with open("logs.txt", "r") as file:
        logs = file.read()

    result = analyze_logs(logs)

    print("\n===== AI ANALYSIS =====\n")
    print(result)
