# log.py — AI.Web Memory Stack Engine
# Stores symbolic memory entries in stack.json
# Supports appending, reading, and stack inspection

import json
from pathlib import Path
from datetime import datetime

STACK_FILE = Path(__file__).parent / "stack.json"
LOG_FILE = Path(__file__).parent / "test_log.txt"

# Ensure the stack file exists
def _init_stack_file():
    if not STACK_FILE.exists():
        STACK_FILE.write_text(json.dumps([], indent=2))
        _log("Initialized empty stack.json")

# Log activity to test_log.txt
def _log(message: str):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# Add a symbolic memory object to the stack
def write_to_stack(data):
    _init_stack_file()
    try:
        stack = json.loads(STACK_FILE.read_text())
        entry = {
            "timestamp": datetime.now().isoformat(),
            "data": data
        }
        stack.append(entry)
        STACK_FILE.write_text(json.dumps(stack, indent=2))
        _log(f"Memory added: {data}")
    except Exception as e:
        _log(f"[ERROR] Failed to write to stack: {e}")
        raise

# Return the full memory stack
def read_stack():
    _init_stack_file()
    try:
        return json.loads(STACK_FILE.read_text())
    except Exception as e:
        _log(f"[ERROR] Failed to read stack: {e}")
        return []
