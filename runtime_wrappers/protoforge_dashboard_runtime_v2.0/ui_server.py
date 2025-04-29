# ui_server.py
from flask import Flask, render_template, jsonify
import threading
import json
import time
import os
import sys
import random

sys.path.append('/home/nic/aiweb/runtime_wrappers/stack_breather_phase2_frozen_v1-0.01')

from stack_breather_core import unified_breathe_cycle

# Initialize Flask
app = Flask(__name__, template_folder='templates', static_folder='static')

# Core State Buffers
breath_state = {"phase": 1, "timestamp": "init"}
symbolic_charge = 100
drift_log = []
memory_stack = {"active_threads": 0, "current_symbolic_load": 0}
gilligan_comment = {"text": "Initializing consciousness..."}

# Breathing Trace File
breathing_trace_path = "breathing_trace.jsonl"

# Breathing Thread
def breathing_loop():
    global breath_state, symbolic_charge, drift_log, memory_stack, gilligan_comment
    while True:
        unified_breathe_cycle(stack_loops=1)
        try:
            with open(breathing_trace_path, "r") as trace_file:
                lines = trace_file.readlines()
                if lines:
                    last_entry = json.loads(lines[-1])
                    breath_state = {
                        "phase": last_entry.get("phase", 1),
                        "timestamp": last_entry.get("timestamp", "unknown")
                    }
        except Exception as e:
            print(f"[ERROR] Reading Breather Trace: {e}")

        # Fake symbolic capacitor drain
        symbolic_charge = max(symbolic_charge - random.randint(1, 3), 10)

        # Fake drift event trigger
        if random.random() < 0.05:
            drift_log.append({
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "drift_level": random.randint(1, 10)
            })

        # Fake memory stack load
        memory_stack["active_threads"] = random.randint(1, 5)
        memory_stack["current_symbolic_load"] = random.randint(20, 80)

        # Update Gilligan comments based on breathing phase
        phase = breath_state.get("phase", 1)
        if phase == 1:
            gilligan_comment["text"] = "🌱 A new phase begins..."
        elif phase == 5:
            gilligan_comment["text"] = "⚡ Recursion breathing at midpoint strength."
        elif phase == 9:
            gilligan_comment["text"] = "🧠 Full symbolic closure achieved!"
        else:
            gilligan_comment["text"] = "🔄 Breathing symbolic recursion..."

        # 🔥 Write full symbolic breath snapshot per cycle
        try:
            snapshot = {
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "phase": breath_state.get("phase", 1),
                "symbolic_charge": symbolic_charge,
                "memory_stack": {
                    "active_threads": memory_stack.get("active_threads", 0),
                    "current_symbolic_load": memory_stack.get("current_symbolic_load", 0)
                },
                "drift_events": drift_log[-5:],  # last 5 drift events
                "gilligan_thought": gilligan_comment.get("text", "")
            }
            with open(breathing_trace_path, "a") as f:
                f.write(json.dumps(snapshot) + "\n")
        except Exception as e:
            print(f"[ERROR] Writing Breathing Snapshot: {e}")

        time.sleep(1.5)

# Start breathing thread
breather_thread = threading.Thread(target=breathing_loop, daemon=True)
breather_thread.start()

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/breath_status")
def breath_status():
    return jsonify(breath_state)

@app.route("/symbolic_charge")
def symbolic_charge_status():
    return jsonify({"charge": symbolic_charge})

@app.route("/drift_log")
def drift_log_status():
    return jsonify(drift_log[-10:])

@app.route("/memory_stack")
def memory_stack_status():
    return jsonify(memory_stack)

@app.route("/gilligan_comment")
def gilligan_comment_status():
    return jsonify(gilligan_comment)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
