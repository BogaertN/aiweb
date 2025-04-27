import os
import json
import time
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def index():
    # Runtime log path
    log_path = "/home/nic/aiweb/runtime_wrappers/protoforge_frozen_v1.06_db_enabled/log/protoforge_log.txt"
    try:
        with open(log_path, "r") as f:
            log_lines = f.readlines()
    except FileNotFoundError:
        log_lines = ["[ERROR] protoforge_log.txt not found."]

    # Field state path
    state_path = "/home/nic/aiweb/runtime_wrappers/protoforge_frozen_v1.06_db_enabled/log/field_state.json"
    try:
        with open(state_path, "r") as f:
            field_state = json.load(f)
    except FileNotFoundError:
        field_state = {"current_phase": "?", "symbolic_charge": 0}

    # Load symbolic charge from capacitor engine
    cap_charge_path = os.path.join(os.path.dirname(__file__), "../engines/symbolic_capacitor_engine_frozen_v1/resonance_sync.json")
    try:
        with open(cap_charge_path, "r") as f:
            cap_data = json.load(f)
            field_state["symbolic_charge"] = cap_data.get("symbolic_charge", 0)
    except Exception as e:
        print(f"[!!] Capacitor read failed: {e}")

    # Drift Arbitration log path
    arbitration_path = "/home/nic/aiweb/runtime_wrappers/protoforge_frozen_v1.06_db_enabled/log/arbitration_log.jsonl"
    arbitration_logs = []
    drift_count = 0
    christping_alert = False

    try:
        with open(arbitration_path, "r") as f:
            for line in f:
                try:
                    event = json.loads(line.strip())
                    arbitration_logs.append(event)

                    # Count drift events
                    if event.get("type") == "DRIFT":
                        drift_count += 1

                    # Detect ChristFunction override
                    if event.get("type") == "CORRECTION" and event.get("severity") == "critical":
                        christping_alert = True
                except json.JSONDecodeError:
                    arbitration_logs.append({
                        "timestamp": "?", "type": "ERROR",
                        "details": "Malformed entry", "severity": "low"
                    })
    except FileNotFoundError:
        arbitration_logs = [{
            "timestamp": "?", "type": "ERROR",
            "details": "arbitration_log.jsonl not found", "severity": "low"
        }]

    # ChristPing Listener Output
    pingback_path = os.path.join(os.path.dirname(__file__), "../engines/christping_listener_frozen_v1/pingback_log.jsonl")
    last_ping = None

    try:
        with open(pingback_path, "r") as f:
            lines = f.readlines()
            if lines:
                last_event = json.loads(lines[-1])
                last_ping = last_event.get("timestamp", "N/A")
    except Exception as e:
        print(f"[!!] ChristPing listener read failed: {e}")

    # Render dashboard
    return render_template(
        "index.html",
        log_lines=log_lines,
        field_state=field_state,
        arbitration_logs=arbitration_logs,
        drift_count=drift_count,
        christping_alert=christping_alert,
        last_ping=last_ping
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)

