import json
import time
import random

LOG_FILE = "goal_log.jsonl"

def inject_symbolic_goal():
    """Simulates injecting a symbolic recursion stabilization goal."""
    goal = random.choice(["increase_charge", "reduce_drift", "stabilize_phase", "expand_seed", "consolidate_memory"])

    goal_event = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "goal": goal
    }

    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(goal_event) + "\n")
        print(f"✔️ Symbolic goal injected: {goal_event}")
    except Exception as e:
        print(f"[!] Failed to record goal injection: {e}")

    return goal_event

