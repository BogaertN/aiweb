import time
import json
import random

CONFIG_PATH = "listener_config.json"
PING_LOG_PATH = "pingback_log.jsonl"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def simulate_entropy():
    return random.uniform(0, 1.0)

def run_listener():
    print("⛓️ ChristPing Listener Activated")

    config = load_config()
    threshold = config.get("entropy_threshold", 0.7)

    entropy = simulate_entropy()
    print(f"→ Symbolic Entropy: {entropy:.3f}")

    if entropy >= threshold:
        event = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "event": "CHRISTPING_TRIGGERED",
            "entropy": entropy,
            "action": "REALIGN_SYSTEM_RECURSION"
        }
        with open(PING_LOG_PATH, "a") as f:
            f.write(json.dumps(event) + "\n")
        print("⚠️ ChristPing triggered — system override ping written")
    else:
        print("✓ Entropy stable — no ping sent")

if __name__ == "__main__":
    run_listener()
