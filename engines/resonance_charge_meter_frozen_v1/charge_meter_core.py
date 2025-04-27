import json
import random
import time

STATE_FILE = "charge_meter_state.json"

def measure_charge():
    """Simulates reading symbolic system charge."""
    simulated_charge = random.randint(30, 100)
    decay_rate = random.uniform(0.01, 0.15)

    reading = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "charge_level": simulated_charge,
        "decay_rate": round(decay_rate, 3)
    }

    try:
        with open(STATE_FILE, "w") as f:
            json.dump(reading, f, indent=2)
        print(f"✔️ Charge measured: {reading}")
    except Exception as e:
        print(f"[!] Failed to write charge state: {e}")

    return reading
