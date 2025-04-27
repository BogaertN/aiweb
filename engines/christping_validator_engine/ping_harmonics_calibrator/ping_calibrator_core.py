# ping_calibrator_core.py
# Ping Harmonics Calibrator Core

class PingHarmonicsCalibrator:
    def __init__(self):
        self.harmonic_adjustments = []

    def calibrate_ping(self, ping_strength, adjustment_factor):
        adjusted = ping_strength * adjustment_factor
        self.harmonic_adjustments.append(adjusted)
        return adjusted

if __name__ == "__main__":
    calibrator = PingHarmonicsCalibrator()
    adjusted = calibrator.calibrate_ping(0.8, 1.05)
    print(f"[TEST] Adjusted Ping Strength: {adjusted}")
