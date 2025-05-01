# ascii_core.py
# Converts symbolic log events into human-readable ASCII summaries

import json
import os
from datetime import datetime

LOG_DIRS = [
    "~/aiweb/engines",  # Can later be narrowed or expanded
]

OUTPUT_FILE = "ascii_trace.log"

def interpret_log_file(log_path):
    try:
        with open(os.path.expanduser(log_path), "r") as f:
            lines = f.readlines()
    except:
        return []

    interpreted = []
    for line in lines:
        try:
            data = json.loads(line.strip())
            timestamp = data.get("timestamp", "N/A")
            summary = f"{timestamp} | Drift={data.get('drift_events', '-')}, Charge={data.get('charge_level', '-')}, Stability={data.get('loop_stability', '-')}"
            interpreted.append(summary)
        except:
            continue
    return interpreted

def write_ascii_summary():
    summaries = []
    for root_dir in LOG_DIRS:
        for subdir, _, files in os.walk(os.path.expanduser(root_dir)):
            for file in files:
                if file.endswith(".json") or file.endswith(".log"):
                    full_path = os.path.join(subdir, file)
                    summaries += interpret_log_file(full_path)

    with open(OUTPUT_FILE, "w") as out:
        for s in summaries:
            out.write(s + "\n")
    print(f"✅ ASCII summary written to {OUTPUT_FILE}")

if __name__ == "__main__":
    write_ascii_summary()
