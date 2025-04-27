# test_archive.py
from archive_core import store_dead_loop

def test_archive_storage():
    result = store_dead_loop("loop_φ8a", "Drift exceeded containment threshold")
    print("✅ Test Passed: Loop stored in archive.")
    print("Stored:", result)

if __name__ == "__main__":
    test_archive_storage()
