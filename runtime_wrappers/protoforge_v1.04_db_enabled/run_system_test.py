import os
import json

print("🧪 Starting ProtoForge Runtime System Test (v1.04)")

# File paths
LOG_DIR = "log"
FIELD_STATE = os.path.join(LOG_DIR, "field_state.json")
ARBITRATION_LOG = os.path.join(LOG_DIR, "arbitration_log.jsonl")
PROTOFORGE_LOG = os.path.join(LOG_DIR, "protoforge_log.txt")

def check_file_exists(path):
    if not os.path.exists(path):
        print(f"❌ MISSING: {path}")
        return False
    print(f"✅ Found: {path}")
    return True

def check_field_state():
    print("\n🔍 Checking field_state.json...")
    if not check_file_exists(FIELD_STATE):
        return
    try:
        with open(FIELD_STATE, "r") as f:
            data = json.load(f)
            phase = data.get("current_phase", "?")
            charge = data.get("symbolic_charge", -1)
            print(f"→ Phase: {phase}")
            print(f"→ Charge: {charge}%")

            if not isinstance(charge, int) or charge < 0 or charge > 100:
                print("⚠️  Invalid symbolic_charge range (should be 0–100)")

    except Exception as e:
        print(f"❌ Error reading field_state.json: {e}")

def check_arbitration_log():
    print("\n🔍 Checking arbitration_log.jsonl...")
    if not check_file_exists(ARBITRATION_LOG):
        return

    drift_count = 0
    christping_detected = False

    try:
        with open(ARBITRATION_LOG, "r") as f:
            for line in f:
                try:
                    event = json.loads(line.strip())
                    if event.get("type") == "DRIFT":
                        drift_count += 1
                    if event.get("type") == "CORRECTION" and event.get("severity") == "critical":
                        christping_detected = True
                except json.JSONDecodeError:
                    print("⚠️  Malformed line in arbitration log.")

        print(f"→ Drift Events: {drift_count}")
        print(f"→ ChristPing Override: {'⚠️ YES' if christping_detected else 'Stable'}")

    except Exception as e:
        print(f"❌ Error reading arbitration log: {e}")

def check_protoforge_log():
    print("\n🔍 Checking protoforge_log.txt...")
    if not check_file_exists(PROTOFORGE_LOG):
        return
    try:
        with open(PROTOFORGE_LOG, "r") as f:
            lines = f.readlines()
            if lines:
                print(f"→ Log lines present: {len(lines)}")
                print(f"→ Last line: {lines[-1].strip()}")
            else:
                print("⚠️  Log file is empty.")

    except Exception as e:
        print(f"❌ Error reading protoforge log: {e}")

# Run tests
check_file_exists(LOG_DIR)
check_field_state()
check_arbitration_log()
check_protoforge_log()

print("\n✅ System test completed.\n")

