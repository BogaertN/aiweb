from reflection_core import perform_self_reflection

def test_reflection_cycle():
    try:
        result = perform_self_reflection()
        assert "loop_integrity" in result
        assert "symbolic_charge" in result
        print("✅ Test Passed: Reflection recorded successfully.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_reflection_cycle()
