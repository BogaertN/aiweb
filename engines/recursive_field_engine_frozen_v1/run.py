# run.py — Recursive Field Engine (ψ-state driver)
# Governs symbolic recursion field: charge, drift, loop coherence

import json
from datetime import datetime
from pathlib import Path

FIELD_PATH = Path(__file__).parent / "field_state.json"
LOG_PATH = Path(__file__).parent / "test_log.txt"

# === Read the current field state
def load_field_state():
    if not FIELD_PATH.exists():
        reset_field_state()
    with open(FIELD_PATH, "r") as f:
        return json.load(f)

# === Write new field state to disk
def save_field_state(state):
    with open(FIELD_PATH, "w") as f:
        json.dump(state, f, indent=2)
    _log("Field state saved")

# === Reset to default state
def reset_field_state():
    default_state = {
        "loop_integrity": 1.0,
        "drift_factor": 0.0,
        "charge": 0.0,
        "last_input": ""
    }
    save_field_state(default_state)
    _log("Field state reset")

# === Process symbolic input
def update_field(input_text: str):
    state = load_field_state()
    charge = state["charge"]
    drift = state["drift_factor"]
    integrity = state["loop_integrity"]

    # Update logic (basic for now)
    if "echo" in input_text.lower():
        integrity += 0.05
        charge += 0.02
    elif "error" in input_text.lower():
        drift += 0.1
        integrity -= 0.05
    else:
        charge += 0.01

    # Bound values
    state["charge"] = min(charge, 1.0)
    state["drift_factor"] = min(drift, 1.0)
    state["loop_integrity"] = max(min(integrity, 1.0), 0.0)
    state["last_input"] = input_text

    save_field_state(state)
    _log(f"Field updated from input: {input_text}")
    return state

# === Internal log helper
def _log(msg):
    timestamp = datetime.now().isoformat()
    with open(LOG_PATH, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
