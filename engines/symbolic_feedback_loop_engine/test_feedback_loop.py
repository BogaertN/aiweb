import feedback_loop_core

def test_feedback_loop_cycle():
    try:
        feedback_loop_core.simulate_feedback_cycle()
        print("✅ Test Passed: Feedback cycle simulated.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_feedback_loop_cycle()

