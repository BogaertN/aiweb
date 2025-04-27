# test_core_system_stack_loader.py
# Tests the core system stack loader

from core_system_stack_loader import load_core_system_stack

def run_test():
    try:
        load_core_system_stack()
        print("✅ Core System Stack Loader Test Passed.")
    except Exception as e:
        print(f"❌ Core System Stack Loader Test Failed: {e}")

if __name__ == "__main__":
    run_test()
