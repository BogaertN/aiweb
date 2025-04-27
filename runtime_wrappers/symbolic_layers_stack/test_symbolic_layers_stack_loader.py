# test_symbolic_layers_stack_loader.py
# Tests the symbolic layers stack loader

from symbolic_layers_stack_loader import load_symbolic_layers_stack

def run_test():
    try:
        load_symbolic_layers_stack()
        print("✅ Symbolic Layers Stack Loader Test Passed.")
    except Exception as e:
        print(f"❌ Symbolic Layers Stack Loader Test Failed: {e}")

if __name__ == "__main__":
    run_test()

