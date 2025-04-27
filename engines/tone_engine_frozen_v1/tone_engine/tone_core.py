import json
import random
import time

STATE_FILE = "tone_state.json"

def determine_tone(charge_level):
    if charge_level > 75:
        return "calm"
    elif 45 <= charge_level <= 75:
        return "focused"
    else:
        return "critical"

def update_tone_state():
    simulated_charge = random.randint(30, 100)
    tone = determine_tone(simulated_charge)

    state = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "charge_level": simulated_charge,
        "tone": tone
    }

    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)
        print(f"✔️ Tone updated: {state}")
    except Exception as e:
        print(f"[!] Failed to write tone state: {e}")

    return state
