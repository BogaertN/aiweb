import json
import time
import random

LOG_FILE = "contribution_log.jsonl"

def simulate_contribution():
    contributor_id = f"agent_{random.randint(1000,9999)}"
    contribution_type = random.choice(["charge_boost", "memory_patch", "correction_ping"])
    contribution_value = random.randint(1, 100)

    event = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "contributor_id": contributor_id,
        "type": contribution_type,
        "value": contribution_value
    }

    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")
        print(f"✔️ Contribution event logged: {event}")
    except Exception as e:
        print(f"[!] Failed to log contribution: {e}")

    return event
