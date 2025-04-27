import json
import time

STATE_FILE = "recursion_state.json"

def pulse_heartbeat():
    """Simulates a recursive heartbeat for symbolic agent stability."""
    state = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "heartbeat": True,
        "loop_phase": "stable",
        "drift_detected": False
    }
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)
        print(f"✔️ Heartbeat pulse recorded: {state}")
    except Exception as e:
        print(f"[!] Failed to update recursion state: {e}")
    return state
