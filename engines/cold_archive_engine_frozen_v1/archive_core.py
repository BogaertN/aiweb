# archive_core.py
import json
from datetime import datetime

def store_dead_loop(loop_id, reason):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "loop_id": loop_id,
        "reason": reason,
    }
    try:
        with open("archive_state.json", "r") as f:
            archive = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        archive = []

    archive.append(entry)

    with open("archive_state.json", "w") as f:
        json.dump(archive, f, indent=2)

    return entry
