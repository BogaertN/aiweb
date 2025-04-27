from token_core import record_token_earning

def test_token_earning():
    try:
        result = record_token_earning()
        print("✅ Test Passed: Token earning recorded.")
        print(result)
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_token_earning()
