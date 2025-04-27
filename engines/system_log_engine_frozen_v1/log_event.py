# log_event.py — AI.Web System Log Engine
# Central runtime event logger. Appends system-level messages to event_log.jsonl
# and mirrors entries to test_log.txt for debug feedback.

import json
from datetime import datetime
from pathlib import Path

EVENT_LOG = Path(__file__).parent / "event_log.jsonl"
TEST_LOG = Path(__file__).parent / "test_log.txt"

def log_event(source: str, message: str, status: str = "info"):
    """Log a system-wide event."""
    timestamp = datetime.now().isoformat()
    entry = {
        "timestamp": timestamp,
        "source": source,
        "status": status,
        "message": message
    }

    # Append to event_log.jsonl (newline-delimited JSON for streaming)
    with open(EVENT_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")

    # Mirror to test_log.txt for debug tracing
    with open(TEST_LOG, "a") as f:
        f.write(f"[{timestamp}] [{status.upper()}] {source}: {message}\n")
