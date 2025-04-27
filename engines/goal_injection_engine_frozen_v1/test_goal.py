from goal_core import inject_symbolic_goal

def test_goal_injection():
    try:
        result = inject_symbolic_goal()
        assert "goal" in result
        print("✅ Test Passed: Symbolic goal injected successfully.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_goal_injection()
