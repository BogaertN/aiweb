# loader.py — AI.Web Plugin Engine
# Discovers and attempts to import any plugin modules from ~/aiweb/plugins/
# Logs load success or failure to test_log.txt

import os
import importlib.util
from pathlib import Path
from datetime import datetime

PLUGIN_DIR = Path(__file__).resolve().parent.parent.parent / "plugins"
LOG_FILE = Path(__file__).parent / "test_log.txt"

def _log(msg):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

def load_plugins():
    _log("Beginning plugin load pass")
    
    if not PLUGIN_DIR.exists():
        _log(f"[ERROR] Plugin directory not found: {PLUGIN_DIR}")
        return

    for file in os.listdir(PLUGIN_DIR):
        if file.endswith(".py") and not file.startswith("_"):
            plugin_path = PLUGIN_DIR / file
            plugin_name = file[:-3]

            try:
                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                _log(f"[OK] Loaded plugin: {plugin_name}")
            except Exception as e:
                _log(f"[FAIL] Failed to load plugin '{plugin_name}': {e}")
