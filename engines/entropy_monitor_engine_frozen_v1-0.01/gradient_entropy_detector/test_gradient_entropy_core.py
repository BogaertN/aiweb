# test_gradient_entropy_core.py

from gradient_entropy_core import GradientEntropyDetector

def test_gradient_entropy_behavior():
    detector = GradientEntropyDetector()
    shift = detector.detect_shift(0.25, 0.30)
    assert shift > 0, "Shift should be positive."
    print("✅ Gradient Entropy Detector Test Passed.")

if __name__ == "__main__":
    test_gradient_entropy_behavior()
