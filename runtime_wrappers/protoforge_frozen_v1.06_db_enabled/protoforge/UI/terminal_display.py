import os

LOG_PATH = os.path.abspath("../../runtime_wrappers/protoforge/log/protoforge_log.txt")

def display_phase(phase_state):
    current = phase_state.get("current_phase", "Φ?")
    print(f"\n🔁 Current Phase: {current}")

def tail_log(lines=10):
    if not os.path.exists(LOG_PATH):
        print("⚠️  Log file not found.")
        return

    with open(LOG_PATH, "r") as f:
        all_lines = f.readlines()
        tail = all_lines[-lines:] if len(all_lines) >= lines else all_lines

    print("\n📄 Recent Log:")
    for line in tail:
        print("   " + line.strip())

