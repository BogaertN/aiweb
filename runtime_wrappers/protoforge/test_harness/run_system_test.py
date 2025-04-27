import sys
import os
import importlib.util

# --- Dynamic Module Loader ---
def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# --- Absolute Paths to Each Frozen Engine ---
base = os.path.abspath("../../engines")

os_engine     = load_module("os_engine",     f"{base}/aiweb_os_engine_frozen_v1/run.py")
phase_engine  = load_module("phase_engine",  f"{base}/phase_engine_frozen_v1/run.py")
tier_enforcer = load_module("tier_enforcer", f"{base}/tier_enforcer_frozen_v1/run.py")
memory_stack  = load_module("memory_stack",  f"{base}/memory_stack_engine_frozen_v1/log.py")
sys_logger    = load_module("sys_logger",    f"{base}/system_log_engine_frozen_v1/log_event.py")
plugin_loader = load_module("plugin_loader", f"{base}/plugin_engine_frozen_v1/loader.py")

print("\n=== 🧪 AI.Web System Test Harness ===")

try:
    print("\n[OS ENGINE] Booting...")
    result = os_engine.execute_command("ping")
    print("OS Engine:", result)
except Exception as e:
    print("OS Engine: FAIL", e)

try:
    print("\n[PHASE ENGINE] Initializing...")
    result = phase_engine.init_phase_state()
    print("Phase Init:", result)
    result = phase_engine.move_to_next_phase()
    print("Phase Step:", result)
except Exception as e:
    print("Phase Engine: FAIL", e)

try:
    print("\n[TIER ENFORCER] Validating output...")
    result = tier_enforcer.enforce_tier("This tool helps you journal clearly.")
    print("Tier Enforcer Output:", result)
except Exception as e:
    print("Tier Enforcer: FAIL", e)

try:
    print("\n[MEMORY STACK] Writing test entry...")
    memory_stack.write_to_stack({"source": "test", "note": "phase step"})
    print("Memory Stack: PASS")
except Exception as e:
    print("Memory Stack: FAIL", e)

try:
    print("\n[SYSTEM LOGGER] Logging system event...")
    sys_logger.log_event("test_harness", "System test running", status="info")
    print("System Logger: PASS")
except Exception as e:
    print("System Logger: FAIL", e)

try:
    print("\n[PLUGIN ENGINE] Attempting to load plugins...")
    plugin_loader.load_plugins()
    print("Plugin Loader: PASS")
except Exception as e:
    print("Plugin Loader: FAIL", e)

print("\n✅ SYSTEM TEST COMPLETE")

