# test_decay_tracker_core.py

from decay_tracker_core import ResonanceDecayTracker

def test_decay_tracker_behavior():
    tracker = ResonanceDecayTracker()
    tracker.record_resonance_value(0.3)
    tracker.record_resonance_value(0.2)
    assert isinstance(tracker.has_active_decay(), bool), "Decay detection should return boolean."
    print("✅ Resonance Decay Tracker Test Passed.")

if __name__ == "__main__":
    test_decay_tracker_behavior()
