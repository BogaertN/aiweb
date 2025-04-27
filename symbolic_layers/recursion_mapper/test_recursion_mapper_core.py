# test_recursion_mapper_core.py

from recursion_mapper_core import RecursionMapper

def test_recursion_mapper_behavior():
    mapper = RecursionMapper()
    record = mapper.map_phase("Φ5", "symbol_anchor_5")
    assert record["phase_id"] == "Φ5", "Phase ID should match."
    assert record["symbolic_anchor"] == "symbol_anchor_5", "Symbolic anchor should match."
    print("✅ Recursion Mapper Test Passed.")

if __name__ == "__main__":
    test_recursion_mapper_behavior()
