# run.py — AI.Web Phase Engine
# Recursive logic controller for FBSC phase transitions (Φ1–Φ9)
# Tracks phase state, detects drift, logs transitions

import json
from pathlib import Path
from datetime import datetime

STATUS_FILE = Path(__file__).parent / "status.json"
LOG_FILE = Path(__file__).parent / "test_log.txt"

PHASE_ORDER = [f"Φ{i}" for i in range(1, 10)]  # Φ1 to Φ9

def _log_event(msg: str):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

def init_phase_state():
    state = {
        "current_phase": "Φ1",
        "history": [],
        "last_updated": datetime.now().isoformat()
    }
    STATUS_FILE.write_text(json.dumps(state, indent=2))
    _log_event("Phase engine initialized at Φ1")
    return state

def get_phase_state():
    if not STATUS_FILE.exists():
        return init_phase_state()
    return json.loads(STATUS_FILE.read_text())

def move_to_next_phase():
    state = get_phase_state()
    current = state["current_phase"]
    try:
        index = PHASE_ORDER.index(current)
    except ValueError:
        _log_event(f"Invalid current_phase value: {current}")
        return {"error": "Invalid phase"}

    if index >= len(PHASE_ORDER) - 1:
        _log_event("Reached Φ9 – loop complete")
        return {"status": "loop_complete", "current_phase": current}

    next_phase = PHASE_ORDER[index + 1]
    state["history"].append(current)
    state["current_phase"] = next_phase
    state["last_updated"] = datetime.now().isoformat()
    STATUS_FILE.write_text(json.dumps(state, indent=2))
    _log_event(f"Phase moved: {current} → {next_phase}")
    return {"status": "moved", "from": current, "to": next_phase}

def force_set_phase(phase: str):
    if phase not in PHASE_ORDER:
        return {"error": f"Invalid phase: {phase}"}
    
    state = get_phase_state()
    state["history"].append(state["current_phase"])
    state["current_phase"] = phase
    state["last_updated"] = datetime.now().isoformat()
    STATUS_FILE.write_text(json.dumps(state, indent=2))
    _log_event(f"Phase force-set to {phase}")
    return {"status": "forced", "phase": phase}
