import os
import sys
from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).parent / "test_log.txt"

def log(msg):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

log("✅ SYSTEM TEST STARTED")

# You can optionally echo a runtime response
log("🧠 System ready to receive input")

log("✅ SYSTEM TEST COMPLETE")
