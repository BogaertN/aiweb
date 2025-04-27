# test_formatter.py
from formatter_core import format_output

def test_format():
    sample = "System initialized."
    result = format_output(sample)
    assert "formatted" in result
    assert "System initialized." in result["formatted"]
    print("✅ Test Passed: Formatter working.")

test_format()
