# decay_tracker_core.py
# Phase 1.5 Engine Standard

class ResonanceDecayTracker:
    def __init__(self):
        self.decay_events = []
        self.decay_threshold = 0.25  # symbolic resonance threshold

    def record_resonance_value(self, value):
        if value < self.decay_threshold:
            self.decay_events.append(value)

    def has_active_decay(self):
        return len(self.decay_events) > 0

if __name__ == "__main__":
    tracker = ResonanceDecayTracker()
    tracker.record_resonance_value(0.2)
    tracker.record_resonance_value(0.4)
    print(f"[TEST] Decay Events: {tracker.decay_events}")
    print(f"[TEST] Active Decay Detected: {tracker.has_active_decay()}")
