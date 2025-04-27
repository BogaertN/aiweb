# recursive_field_core.py
# Phase 1.5 Recursive Field Engine Core

class RecursiveFieldEngine:
    def __init__(self):
        self.field_state = []

    def inject_symbolic_value(self, value):
        self.field_state.append(value)

    def field_size(self):
        return len(self.field_state)

if __name__ == "__main__":
    rfe = RecursiveFieldEngine()
    rfe.inject_symbolic_value("symbolic_seed")
    print(f"[TEST] Field Size: {rfe.field_size()}")
