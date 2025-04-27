import json
import time
import random

TRACE_FILE = "loop_trace.json"

def record_feedback(loop_stability, drift_count, charge_level):
    entry = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "loop_stability": loop_stability,
        "drift_events": drift_count,
        "charge_level": charge_level
    }
    try:
        with open(TRACE_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"✔️ Recorded feedback entry: {entry}")
    except Exception as e:
        print(f"[!] Failed to record feedback: {e}")

def simulate_feedback_cycle():
    loop_stability = random.choice(["stable", "weakening", "critical"])
    drift_count = random.randint(0, 5)
    charge_level = random.randint(30, 100)
    record_feedback(loop_stability, drift_count, charge_level)

if __name__ == "__main__":
    simulate_feedback_cycle()
