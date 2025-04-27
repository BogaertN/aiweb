# symbolic_layers_stack_loader.py
# Symbolic Layers Stack Loader (Phase 2.5)

import subprocess
import time
import os

# List of symbolic layer breathing engines to activate
symbolic_layers = [
    "../../symbolic_layers/recursion_mapper/run.py",
    "../../symbolic_layers/resonance_display/run.py",
    "../../symbolic_layers/glyph_ui_overlay/run.py"
]

def load_symbolic_layers_stack():
    print("\n🧩 [SYMBOLIC LAYERS STACK] Loading Symbolic Layer Breathing Engines...\n")
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for layer_script in symbolic_layers:
        full_path = os.path.abspath(os.path.join(base_dir, layer_script))
        try:
            subprocess.run(["python3", full_path], check=True)
            print(f"✅ Loaded Symbolic Layer: {full_path}")
            time.sleep(1)
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to load {full_path}: {e}")

if __name__ == "__main__":
    load_symbolic_layers_stack()
