# run.py
# AI.Web Plugin Engine - Phase 1.5 real runtime

import os

def load_plugins():
    plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "plugins"))

    if not os.path.exists(plugin_dir):
        print("⚠️ [PLUGIN ENGINE] No plugins directory found.")
        return

    plugins = [f for f in os.listdir(plugin_dir) if f.endswith(".py")]

    if not plugins:
        print("⚠️ [PLUGIN ENGINE] No plugins to load.")
        return

    for plugin in plugins:
        print(f"✅ [PLUGIN ENGINE] Found Plugin: {plugin}")

def start_plugin_engine():
    print("🔵 [PLUGIN ENGINE] Plugin Engine Runtime Starting...")
    load_plugins()
    print("✅ [PLUGIN ENGINE] Plugin Engine Ready.\n")

if __name__ == "__main__":
    start_plugin_engine()

