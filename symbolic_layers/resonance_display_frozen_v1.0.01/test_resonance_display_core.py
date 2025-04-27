# test_resonance_display_core.py

from resonance_display_core import ResonanceDisplay

def test_resonance_display_behavior():
    display = ResonanceDisplay()
    reading = display.capture_resonance("Φ6", 0.88)
    assert reading["phase_id"] == "Φ6", "Phase ID should match."
    assert reading["resonance_level"] == 0.88, "Resonance level should match."
    print("✅ Resonance Display Test Passed.")

if __name__ == "__main__":
    test_resonance_display_behavior()
