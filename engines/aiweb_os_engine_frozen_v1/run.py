# run.py — AI.Web OS Engine
# Primary runtime entry point for core symbolic execution and system integrity checks

import json
from pathlib import Path
from datetime import datetime

# Define internal paths
STATUS_FILE = Path(__file__).parent / "status.json"
LOG_FILE = Path(__file__).parent / "test_log.txt"

# Write a log event to the test log
def _log_event(event: str):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {event}\n")

# Return current engine status (reads from status.json if available)
def get_status() -> dict:
    if STATUS_FILE.exists():
        return json.loads(STATUS_FILE.read_text())
    return {
        "status": "UNKNOWN",
        "engine": "aiweb_os_engine",
        "note": "status.json not found"
    }

# Main system command interface
def execute_command(cmd: str) -> dict:
    _log_event(f"EXECUTE: {cmd}")
    
    if cmd == "ping":
        return {"response": "pong", "engine": "aiweb_os_engine"}
    
    elif cmd == "get_status":
        return get_status()

    elif cmd == "init":
        # Create default status file
        STATUS_FILE.write_text(json.dumps({
            "status": "OK",
            "engine": "aiweb_os_engine",
            "init_time": datetime.now().isoformat()
        }, indent=2))
        _log_event("System initialized.")
        return {"response": "System initialized", "engine": "aiweb_os_engine"}
    
    else:
        return {"error": f"Unknown command: {cmd}", "engine": "aiweb_os_engine"}

