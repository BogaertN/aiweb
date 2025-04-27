# admin_override_core.py
# Admin Override Console Core

class AdminOverrideConsole:
    def __init__(self):
        self.override_logs = []

    def execute_override(self, command_type, target):
        override_record = {
            "command_type": command_type,
            "target": target
        }
        self.override_logs.append(override_record)
        return override_record

if __name__ == "__main__":
    console = AdminOverrideConsole()
    record = console.execute_override("shutdown", "recursion_field_01")
    print(f"[TEST] Override Command Executed: {record}")
