from dream_core import simulate_dream_state

def test_dream_generation():
    try:
        result = simulate_dream_state()
        assert "drift_intensity" in result
        assert "dream_signature" in result
        print("✅ Test Passed: Dream state event recorded successfully.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_dream_generation()
