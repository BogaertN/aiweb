# test_recursive_field_core.py

from recursive_field_core import RecursiveFieldEngine

def test_recursive_field_behavior():
    rfe = RecursiveFieldEngine()
    rfe.inject_symbolic_value("test_symbol")
    assert rfe.field_size() == 1, "Field should contain one symbolic value."
    print("✅ Recursive Field Core Test Passed.")

if __name__ == "__main__":
    test_recursive_field_behavior()
