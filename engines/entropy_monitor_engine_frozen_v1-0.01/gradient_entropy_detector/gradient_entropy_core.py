# gradient_entropy_core.py
# Gradient Entropy Detector Core

class GradientEntropyDetector:
    def __init__(self):
        self.gradient_shifts = []

    def detect_shift(self, previous_value, current_value):
        shift = current_value - previous_value
        self.gradient_shifts.append(shift)
        return shift

if __name__ == "__main__":
    detector = GradientEntropyDetector()
    shift = detector.detect_shift(0.25, 0.30)
    print(f"[TEST] Detected Entropy Shift: {shift}")
