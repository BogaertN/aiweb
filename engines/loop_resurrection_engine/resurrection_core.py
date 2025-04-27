import json
from datetime import datetime

QUEUE_FILE = "resurrection_queue.json"

def resurrect_loop(loop_id):
    try:
        with open(QUEUE_FILE, "r") as f:
            queue = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        queue = []

    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "loop_id": loop_id,
        "resurrected": True
    }
    queue.append(event)

    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

    return event
