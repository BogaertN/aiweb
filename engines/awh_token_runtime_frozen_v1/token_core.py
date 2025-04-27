import json
import time
import random

LEDGER_FILE = "token_ledger.json"

def record_token_earning():
    """
    Simulates calculation of earned tokens based on uptime and simulated load.
    """
    # Simulated uptime in hours and load percentage
    uptime_hours = random.uniform(1, 10)       # for example, 1 to 10 hours
    cpu_load = random.randint(30, 100)           # load percentage
    # Simple formula: tokens = (uptime * cpu_load) / constant factor
    tokens_earned = round((uptime_hours * cpu_load) / 100, 3)
    
    event = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "uptime_hours": round(uptime_hours, 2),
        "cpu_load": cpu_load,
        "tokens_earned": tokens_earned
    }
    
    try:
        # Append the event to the ledger file (as a new JSON line)
        with open(LEDGER_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")
        print(f"✔️ Recorded token earning: {event}")
    except Exception as e:
        print(f"[!] Failed to update token ledger: {e}")
    
    return event
