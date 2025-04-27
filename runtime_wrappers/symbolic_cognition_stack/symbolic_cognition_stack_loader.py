# symbolic_cognition_stack_loader.py
# Symbolic Cognition Stack Loader (Phase 2)

import subprocess
import time
import os

# List of frozen engine run paths
frozen_engines = [
    "../../engines/symbolic_feedback_loop_engine_frozen_v1/run.py",
    "../../engines/cold_archive_engine_frozen_v1/run.py",
    "../../engines/loop_resurrection_engine_frozen_v1/run.py",
    "../../engines/resonance_charge_meter_frozen_v1/run.py"
]

def load_symbolic_cognition_stack():
    print("\n🧠 [SYMBOLIC COGNITION STACK] Loading Symbolic Cognition Engines...\n")
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
    load_symbolic_cognition_stack()
