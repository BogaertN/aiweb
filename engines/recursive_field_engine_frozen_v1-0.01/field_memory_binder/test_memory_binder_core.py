# test_memory_binder_core.py

from memory_binder_core import FieldMemoryBinder

def test_memory_binder_behavior():
    binder = FieldMemoryBinder()
    binder.bind_memory(["symbolic_state_1"])
    assert binder.get_memory_count() == 1, "Memory binder should store one snapshot."
    print("✅ Field Memory Binder Test Passed.")

if __name__ == "__main__":
    test_memory_binder_behavior()
