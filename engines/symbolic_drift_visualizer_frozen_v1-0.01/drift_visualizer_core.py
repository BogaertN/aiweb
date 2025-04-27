# drift_visualizer_core.py
# Phase 1.5 Symbolic Drift Visualizer Core

class SymbolicDriftVisualizer:
    def __init__(self):
        self.drift_log = []

    def record_drift_event(self, field_name, drift_amount):
        self.drift_log.append({
            "field": field_name,
            "drift": drift_amount
        })

    def get_total_drift_events(self):
        return len(self.drift_log)

if __name__ == "__main__":
    visualizer = SymbolicDriftVisualizer()
    visualizer.record_drift_event("ψ-anchor", 0.07)
    print(f"[TEST] Total Drift Events Recorded: {visualizer.get_total_drift_events()}")
