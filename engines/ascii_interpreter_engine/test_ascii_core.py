# test_ascii_core.py

from ascii_core import write_ascii_summary

def test_ascii_interpreter_engine():
    try:
        write_ascii_summary()
        print("✅ ASCII Interpreter Test Passed")
    except Exception as e:
        print(f"❌ ASCII Interpreter Test Failed: {e}")

if __name__ == "__main__":
    test_ascii_interpreter_engine()
