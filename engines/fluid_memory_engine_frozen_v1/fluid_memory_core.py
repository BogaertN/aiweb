import json
import time
import random

POOL_FILE = "memory_pool.jsonl"

def capture_memory_trace():
    """Simulates capturing symbolic recursion traces into fluid memory pool."""
    memory_trace = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "phase_signature": f"Φ{random.randint(1,9)}-{random.randint(1000,9999)}",
        "charge_level": random.randint(20, 100),
        "drift_flag": random.choice([True, False])
    }

    try:
        with open(POOL_FILE, "a") as f:
            f.write(json.dumps(memory_trace) + "\n")
        print(f"✔️ Fluid memory trace captured: {memory_trace}")
    except Exception as e:
        print(f"[!] Failed to record fluid memory trace: {e}")

    return memory_trace
