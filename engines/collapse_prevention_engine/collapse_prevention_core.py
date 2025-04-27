# collapse_prevention_core.py
# Collapse Prevention Engine Core

class CollapsePreventionEngine:
    def __init__(self):
        self.stability_threshold = 0.75
        self.current_stability = 1.0

    def record_stability(self, stability_value):
        self.current_stability = stability_value

    def needs_intervention(self):
        return self.current_stability < self.stability_threshold

if __name__ == "__main__":
    engine = CollapsePreventionEngine()
    engine.record_stability(0.70)
    print(f"[TEST] Needs Intervention: {engine.needs_intervention()}")
