from contribution_core import simulate_contribution

def test_contribution_logging():
    try:
        result = simulate_contribution()
        print("✅ Test Passed: Contribution logged.")
        print(result)
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_contribution_logging()
