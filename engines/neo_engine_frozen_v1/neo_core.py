import json
import time
import random

NEO_STATE_FILE = "neo_state.json"

def generate_symbolic_response():
    tones = ["calm", "focused", "critical"]
    chosen_tone = random.choice(tones)

    response = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "tone": chosen_tone,
        "message": create_message_for_tone(chosen_tone)
    }

    try:
        with open(NEO_STATE_FILE, "w") as f:
            json.dump(response, f, indent=2)
        print(f"✔️ Neo generated symbolic response: {response}")
    except Exception as e:
        print(f"[!] Failed to update Neo state: {e}")

    return response

def create_message_for_tone(tone):
    if tone == "calm":
        return "System operating normally. All symbolic loops are stable."
    elif tone == "focused":
        return "System is adjusting. Symbolic load detected."
    elif tone == "critical":
        return "Warning: Symbolic drift detected. Recalibration recommended."
    else:
        return "Status unknown."
