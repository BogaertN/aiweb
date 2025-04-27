# test_symbolic_cognition_stack_loader.py
# Tests the upgraded symbolic cognition stack loader

from symbolic_cognition_stack_loader import load_symbolic_cognition_stack

def run_test():
    try:
        load_symbolic_cognition_stack()
        print("✅ Symbolic Cognition Stack Loader Test Passed.")
    except Exception as e:
        print(f"❌ Symbolic Cognition Stack Loader Test Failed: {e}")

if __name__ == "__main__":
    run_test()
