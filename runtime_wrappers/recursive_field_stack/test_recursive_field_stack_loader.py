# test_recursive_field_stack_loader.py
# Tests the recursive field stack loader

from recursive_field_stack_loader import load_recursive_field_stack

def run_test():
    try:
        load_recursive_field_stack()
        print("✅ Recursive Field Stack Loader Test Passed.")
    except Exception as e:
        print(f"❌ Recursive Field Stack Loader Test Failed: {e}")

if __name__ == "__main__":
    run_test()
