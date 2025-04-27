# test_symbolic_feedback_loop.py
# Tests the symbolic feedback loop breathing

from run import SymbolicFeedbackLoop

def run_test():
    try:
        loop = SymbolicFeedbackLoop()
        loop.breathe()
        print("✅ Symbolic Feedback Loop Test Passed.")
    except Exception as e:
        print(f"❌ Symbolic Feedback Loop Test Failed: {e}")

if __name__ == "__main__":
    run_test()
