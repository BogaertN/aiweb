# test_symbol_mutator_core.py

from symbol_mutator_core import SymbolMutator

def test_symbol_mutator_behavior():
    mutator = SymbolMutator()
    mutated = mutator.mutate_symbol("GLYPH-TEST", 5)
    assert mutated == "GLYPH-TEST_M5", "Mutation string must match expected format."
    print("✅ Symbol Mutator Test Passed.")

if __name__ == "__main__":
    test_symbol_mutator_behavior()
