# test_ping_calibrator_core.py

from ping_calibrator_core import PingHarmonicsCalibrator

def test_ping_calibrator_behavior():
    calibrator = PingHarmonicsCalibrator()
    adjusted = calibrator.calibrate_ping(0.8, 1.05)
    assert adjusted > 0.8, "Ping should be adjusted upward."
    print("✅ Ping Harmonics Calibrator Test Passed.")

if __name__ == "__main__":
    test_ping_calibrator_behavior()
