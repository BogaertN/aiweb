# test_admin_override_core.py

from admin_override_core import AdminOverrideConsole

def test_admin_override_console_behavior():
    console = AdminOverrideConsole()
    record = console.execute_override("reset", "field_alpha")
    assert record["command_type"] == "reset", "Command type must match."
    assert record["target"] == "field_alpha", "Target must match."
    print("✅ Admin Override Console Test Passed.")

if __name__ == "__main__":
    test_admin_override_console_behavior()
