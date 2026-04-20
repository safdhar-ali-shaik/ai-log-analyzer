import time
import os

def follow(file_path):
    # Wait until file exists
    while not os.path.exists(file_path):
        print("Waiting for log file...")
        time.sleep(1)

    with open(file_path, "r") as file:
        file.seek(0, 2)  # move to end

        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line.strip()