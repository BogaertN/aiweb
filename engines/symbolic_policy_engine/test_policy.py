from policy_core import enforce_symbolic_policies

def test_policy_enforcement():
    try:
        result = enforce_symbolic_policies()
        assert "rules_enforced" in result
        assert isinstance(result["rules_enforced"], dict)
        print("✅ Test Passed: Symbolic policies enforced successfully.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_policy_enforcement()
