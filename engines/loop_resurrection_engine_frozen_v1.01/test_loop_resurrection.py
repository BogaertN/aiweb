# test_loop_resurrection.py
# Tests the loop resurrection behavior

from run import LoopResurrectionEngine

def run_test():
    try:
        resurrection = LoopResurrectionEngine()
        for i in range(2):
            resurrection.resurrect_loop(f"test_cold_loop_{i+1}")
        resurrection.resurrection_summary()
        print("✅ Loop Resurrection Engine Test Passed.")
    except Exception as e:
        print(f"❌ Loop Resurrection Engine Test Failed: {e}")

if __name__ == "__main__":
    run_test()
