# resonance_display_core.py
# Resonance Display Core

class ResonanceDisplay:
    def __init__(self):
        self.resonance_readings = []

    def capture_resonance(self, phase_id, resonance_level):
        reading = {
            "phase_id": phase_id,
            "resonance_level": resonance_level
        }
        self.resonance_readings.append(reading)
        return reading

if __name__ == "__main__":
    display = ResonanceDisplay()
    reading = display.capture_resonance("Φ2", 0.93)
    print(f"[TEST] Resonance Reading: {reading}")
