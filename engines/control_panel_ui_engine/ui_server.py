import json

# ui_server.py
# Flask server for Control Panel UI Engine (log viewer enabled)

from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def index():
    # Runtime log path
    log_path = "/home/nic/aiweb/engines/protoforge_frozen_v1.03_os_ui_rfe_dae/protoforge_log.txt"
    try:
        with open(log_path, "r") as f:
            log_lines = f.readlines()
    except FileNotFoundError:
        log_lines = ["[ERROR] protoforge_log.txt not found."]

    # Field state path
    state_path = "/home/nic/aiweb/engines/protoforge_frozen_v1.03_os_ui_rfe_dae/field_state.json"
    try:
        with open(state_path, "r") as f:
            field_state = json.load(f)
    except FileNotFoundError:
        field_state = {"current_phase": "?", "symbolic_charge": 0}

    # Arbitration log path — move this here
    arbitration_path = "/home/nic/aiweb/engines/protoforge_frozen_v1.03_os_ui_rfe_dae/arbitration_log.jsonl"
    arbitration_logs = []
    try:
        with open(arbitration_path, "r") as f:
            for line in f:
                try:
                    arbitration_logs.append(json.loads(line.strip()))
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
        arbitration_logs=arbitration_logs
    )

    # Arbitration log path
    arbitration_path = "/home/nic/aiweb/engines/protoforge_frozen_v1.03_os_ui_rfe_dae/arbitration_log.jsonl"
    arbitration_logs = []
    try:
        with open(arbitration_path, "r") as f:
            for line in f:
                try:
                    arbitration_logs.append(json.loads(line.strip()))
                except json.JSONDecodeError:
                    arbitration_logs.append({"timestamp": "?", "type": "ERROR", "details": "Malformed entry", "severity": "low"})
    except FileNotFoundError:
        arbitration_logs = [{"timestamp": "?", "type": "ERROR", "details": "arbitration_log.jsonl not found", "severity": "low"}]

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)

