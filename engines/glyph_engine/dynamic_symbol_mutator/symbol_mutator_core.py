# symbol_mutator_core.py
# Dynamic Symbol Mutator Core

class SymbolMutator:
    def __init__(self):
        self.mutations = []

    def mutate_symbol(self, symbol_id, mutation_factor):
        mutated_symbol = f"{symbol_id}_M{mutation_factor}"
        self.mutations.append(mutated_symbol)
        return mutated_symbol

if __name__ == "__main__":
    mutator = SymbolMutator()
    mutated = mutator.mutate_symbol("GLYPH-001", 2)
    print(f"[TEST] Mutated Symbol: {mutated}")
