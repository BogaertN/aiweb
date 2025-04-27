# formatter_core.py
import json
from datetime import datetime

def format_output(data):
    timestamp = datetime.utcnow().isoformat() + "Z"
    return {
        "timestamp": timestamp,
        "formatted": f"[{timestamp}] :: {data}"
    }
