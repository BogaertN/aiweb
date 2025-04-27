import json
import time
import random

LOG_FILE = "naming_log.jsonl"

def assign_symbolic_name():
    """Simulates phase-driven symbolic naming event."""
    phase = random.choice(["Φ1", "Φ2", "Φ3", "Φ4", "Φ5", "Φ6", "Φ7", "Φ8", "Φ9"])
    symbolic_name = f"Phase_{phase}_Node_{random.randint(100,999)}"

    naming_event = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "assigned_name": symbolic_name,
        "phase": phase
    }

    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(naming_event) + "\n")
        print(f"✔️ Symbolic name assigned: {naming_event}")
    except Exception as e:
        print(f"[!] Failed to record naming event: {e}")

    return naming_event
