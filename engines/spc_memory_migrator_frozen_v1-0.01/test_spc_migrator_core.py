# test_spc_migrator_core.py

from spc_migrator_core import SPCMemoryMigrator

def test_spc_memory_migrator_behavior():
    migrator = SPCMemoryMigrator()
    record = migrator.migrate_memory("test_mem", "target_stack")
    assert record["memory_id"] == "test_mem", "Memory ID should match."
    assert record["target_stack"] == "target_stack", "Target stack should match."
    print("✅ SPC Memory Migrator Test Passed.")

if __name__ == "__main__":
    test_spc_memory_migrator_behavior()
