# core_system_stack_loader.py
# Core System Stack Loader (Phase 2)

import subprocess
import time
import os

# List of frozen engine run paths
frozen_engines = [
    "../../engines/aiweb_os_engine_frozen_v1/run.py",
    "../../engines/phase_engine_frozen_v1/run.py",
    "../../engines/tier_enforcer_frozen_v1/run.py",
    "../../engines/plugin_engine_frozen_v1/run.py"
]

def load_core_system_stack():
    print("\n🔵 [CORE STACK] Loading AI.Web Core System Engines...\n")
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
    load_core_system_stack()
