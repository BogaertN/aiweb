# recursive_field_stack_loader.py
# Recursive Field Stack Loader (Phase 2)

import subprocess
import time
import os

# List of frozen engine run paths
frozen_engines = [
    "../../engines/recursive_field_engine_frozen_v1/run.py",
    "../../engines/drift_arbitration_engine_frozen_v1/run.py",
    "../../engines/memory_stack_engine/spiral_drift_controller_frozen_v1-0.01/drift_angle_monitor.py"
]

def load_recursive_field_stack():
    print("\n🌀 [RECURSIVE FIELD STACK] Loading Recursive Symbolic Field Engines...\n")
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for engine_script in frozen_engines:
        full_path = os.path.abspath(os.path.join(base_dir, engine_script))
        try:
            subprocess.run(["python3", full_path], check=True)
            print(f"✅ Loaded: {full_path}")
            time.sleep(1)
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to load {full_path}: {e}")

if __name__ == "__main__":
    load_recursive_field_stack()
