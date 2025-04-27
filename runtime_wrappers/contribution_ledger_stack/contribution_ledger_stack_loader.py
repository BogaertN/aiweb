# contribution_ledger_stack_loader.py
# Contribution Ledger Stack Loader (Phase 2.5)

import json
import time
import os

user_registry_path = os.path.join(os.path.dirname(__file__), "user_registry.json")
contribution_log_path = os.path.join(os.path.dirname(__file__), "contribution_log.jsonl")

def load_user_registry():
    if not os.path.exists(user_registry_path):
        print("❌ [LEDGER] No user registry found!")
        return {}
    with open(user_registry_path, "r") as f:
        return json.load(f)

def save_user_registry(registry):
    with open(user_registry_path, "w") as f:
        json.dump(registry, f, indent=2)

def signup_new_user(username):
    registry = load_user_registry()
    next_id = str(max([int(uid) for uid in registry.keys()]) + 1)
    registry[next_id] = {
        "username": username,
        "joined_on": time.strftime("%Y-%m-%d")
    }
    save_user_registry(registry)
    print(f"✅ [LEDGER] User '{username}' registered with ID {next_id}")

def log_contribution(user_id, action_description):
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": user_id,
        "action": action_description
    }
    with open(contribution_log_path, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"📝 [LEDGER] Logged contribution: {entry}")

def run_contribution_ledger():
    print("\n🔵 [LEDGER] Contribution Ledger Stack Activated...\n")
    registry = load_user_registry()

    while True:
        print("\nOptions:\n1. Log Contribution (Founder_Nic)\n2. Sign Up New User\n3. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            action = input("Describe your contribution action: ").strip()
            log_contribution("1", action)  # Founder_Nic is always ID 1
        elif choice == "2":
            new_username = input("Enter new username: ").strip()
            signup_new_user(new_username)
        elif choice == "3":
            print("✅ [LEDGER] Exiting Contribution Ledger.")
            break
        else:
            print("⚠️ Invalid option.")

if __name__ == "__main__":
    run_contribution_ledger()
