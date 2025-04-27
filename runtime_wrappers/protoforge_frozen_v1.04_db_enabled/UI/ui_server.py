import json

# ui_server.py
# Flask server for Control Panel UI Engine (log viewer enabled)

from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def index():
    # Runtime log path
    log_path = "/home/nic/aiweb/runtime_wrappers/protoforge_v1.04_db_enabled/log/protoforge_log.txt"
    try:
        with open(log_path, "r") as f:
            log_lines = f.readlines()
    except FileNotFoundError:
        log_lines = ["[ERROR] protoforge_log.txt not found."]

    # Field state path
    state_path = "/home/nic/aiweb/runtime_wrappers/protoforge_v1.04_db_enabled/log/field_state.json"
    try:
        with open(state_path, "r") as f:
            field_state = json.load(f)
    except FileNotFoundError:
        field_state = {"current_phase": "?", "symbolic_charge": 0}

    # Drift Arbitration log path
    arbitration_path = "/home/nic/aiweb/runtime_wrappers/protoforge_v1.04_db_enabled/log/field_state.json"
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

    return render_template(
        "index.html",
        log_lines=log_lines,
        field_state=field_state,
        arbitration_logs=arbitration_logs,
        drift_count=drift_count,
        christping_alert=christping_alert
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)

