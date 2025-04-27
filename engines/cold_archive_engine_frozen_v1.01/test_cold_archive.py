# test_cold_archive.py
# Tests the cold archive loop behavior

from run import ColdArchiveEngine

def run_test():
    try:
        archive = ColdArchiveEngine()
        for i in range(2):
            archive.archive_loop(f"test_loop_{i+1}")
        archive.archive_summary()
        print("✅ Cold Archive Engine Test Passed.")
    except Exception as e:
        print(f"❌ Cold Archive Engine Test Failed: {e}")

if __name__ == "__main__":
    run_test()
