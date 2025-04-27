# run.py — Drift Arbitration Engine
# Monitors loop integrity and drift factor from recursive_field_engine
# Detects recursion violations (e.g. 5→8 symbolic skips) and logs arbitration events

import json
from datetime import datetime
from pathlib import Path

# Paths
FIELD_PATH = Path("../../engines/recursive_field_engine/field_state.json").resolve()
ARBITRATION_LOG = Path(__file__).parent / "arbitration_log.jsonl"
TEST_LOG = Path(__file__).parent / "test_log.txt"

# Thresholds
DRIFT_THRESHOLD = 0.30
INTEGRITY_MINIMUM = 0.70
AUTO_CORRECT = False  # set to True to allow auto reset

# === Load current field state from recursive field engine
def load_field():
    with open(FIELD_PATH, "r") as f:
        return json.load(f)

# === Detect drift based on symbolic thresholds
def detect_drift():
    state = load_field()
    drift = state["drift_factor"]
    integrity = state["loop_integrity"]
    current_input = state.get("last_input", "")

    if drift >= DRIFT_THRESHOLD and integrity <= INTEGRITY_MINIMUM:
        log_event("DRIFT_DETECTED", state)
        if AUTO_CORRECT:
            from pathlib import Path
            reset_path = Path("../../engines/recursive_field_engine/run.py").resolve()
            exec(open(reset_path).read(), {"__name__": "__main__"})
            log_event("AUTO_CORRECT_TRIGGERED", {"message": "Field reset issued."})
            return {"status": "corrected", "input": current_input}
        else:
            return {"status": "drift_detected", "input": current_input}
    else:
        return {"status": "stable", "input": current_input}

# === Append arbitration event to log
def log_event(event_type, data):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        "data": data
    }
    with open(ARBITRATION_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")

    with open(TEST_LOG, "a") as log:
        log.write(f"[{entry['timestamp']}] {event_type} — {entry['data']}\n")
