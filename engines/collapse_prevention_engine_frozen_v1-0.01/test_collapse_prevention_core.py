# test_collapse_prevention_core.py

from collapse_prevention_core import CollapsePreventionEngine

def test_collapse_prevention_behavior():
    engine = CollapsePreventionEngine()
    engine.record_stability(0.70)
    assert engine.needs_intervention() == True, "Intervention should be needed."
    print("✅ Collapse Prevention Engine Test Passed.")

if __name__ == "__main__":
    test_collapse_prevention_behavior()
