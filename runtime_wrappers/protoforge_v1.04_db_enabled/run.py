import os
import importlib.util
from datetime import datetime

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# === Load All Engines ===
base = os.path.abspath("../../engines")
os_engine     = load_module("os_engine",     f"{base}/aiweb_os_engine_frozen_v1/run.py")
phase_engine  = load_module("phase_engine",  f"{base}/phase_engine_frozen_v1/run.py")
tier_enforcer = load_module("tier_enforcer", f"{base}/tier_enforcer_frozen_v1/run.py")
memory_stack  = load_module("memory_stack",  f"{base}/memory_stack_engine_frozen_v1/log.py")
sys_logger    = load_module("sys_logger",    f"{base}/system_log_engine_frozen_v1/log_event.py")
plugin_loader = load_module("plugin_loader", f"{base}/plugin_engine_frozen_v1/loader.py")

# === Load UI Display Module ===
from UI.terminal_display import display_phase, tail_log

# === Boot Message ===
print("\n🚀 Welcome to AI.Web – ProtoForge Runtime v1")
print("Type 'exit' to shut down. All commands are logged.\n")

# === Ping Engines ===
os_engine.execute_command("ping")
phase_engine.init_phase_state()
plugin_loader.load_plugins()

# === Runtime Loop ===
while True:
    try:
        user_input = input("🧠 > ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting ProtoForge runtime...")
            sys_logger.log_event("protoforge", "System shutdown requested", status="info")
            break

        # Phase system reacts
        phase_engine.move_to_next_phase()

        # Enforce tiers
        clean_output = tier_enforcer.enforce_tier(user_input)

        # Memory log
        memory_stack.write_to_stack({
            "timestamp": datetime.now().isoformat(),
            "source": "user",
            "event": "input",
            "content": clean_output
        })

        # Log system event
        sys_logger.log_event("protoforge", f"Received input: {user_input}", status="info")

	# Show Phase + Log
        phase_state = phase_engine.get_phase_state()
        display_phase(phase_state)
        tail_log(lines=6)

        # Echo result
        print(f"✅ {clean_output}")

        with open("log/protoforge_log.txt", "a") as f:
            f.write(f"[{datetime.now().isoformat()}] {clean_output}\n")

    except Exception as e:
        print("⚠️ Error:", e)
        sys_logger.log_event("protoforge", f"Runtime error: {e}", status="error")
