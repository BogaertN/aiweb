from naming_core import assign_symbolic_name

def test_naming_cycle():
    try:
        result = assign_symbolic_name()
        assert "assigned_name" in result
        assert "phase" in result
        print("✅ Test Passed: Symbolic name assigned successfully.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_naming_cycle()
