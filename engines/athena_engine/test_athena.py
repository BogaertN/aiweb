from athena_core import system_introspection

def test_athena_selfcheck():
    try:
        result = system_introspection()
        assert "recursion_health" in result
        assert "drift_alert" in result
        print("✅ Test Passed: Athena system introspection complete.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_athena_selfcheck()
