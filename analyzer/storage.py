import json
from datetime import datetime

OUTPUT_FILE = "data/output.json"

def save_result(result):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        **result
    }

    try:
        with open(OUTPUT_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)