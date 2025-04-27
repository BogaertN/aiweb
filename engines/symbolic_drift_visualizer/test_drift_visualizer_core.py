# test_drift_visualizer_core.py

from drift_visualizer_core import SymbolicDriftVisualizer

def test_drift_visualizer_behavior():
    visualizer = SymbolicDriftVisualizer()
    visualizer.record_drift_event("test_field", 0.05)
    assert visualizer.get_total_drift_events() == 1, "Drift event should be recorded."
    print("✅ Symbolic Drift Visualizer Test Passed.")

if __name__ == "__main__":
    test_drift_visualizer_behavior()
