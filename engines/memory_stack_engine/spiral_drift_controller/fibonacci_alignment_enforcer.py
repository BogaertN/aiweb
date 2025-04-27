# fibonacci_alignment_enforcer.py
# Enforces drift spiral alignment toward Fibonacci ratio

class FibonacciAlignmentEnforcer:
    def __init__(self, ideal_ratio=1.618, tolerance=0.05):
        self.ideal_ratio = ideal_ratio
        self.tolerance = tolerance

    def check_alignment(self, drift_ratio):
        lower = self.ideal_ratio * (1 - self.tolerance)
        upper = self.ideal_ratio * (1 + self.tolerance)
        return lower <= drift_ratio <= upper

    def calculate_correction_pressure(self, drift_ratio):
        deviation = abs(drift_ratio - self.ideal_ratio)
        return min(deviation / self.ideal_ratio, 1.0)

if __name__ == "__main__":
    enforcer = FibonacciAlignmentEnforcer()
    print(f"[TEST] Alignment Check (1.6): {enforcer.check_alignment(1.6)}")
    print(f"[TEST] Correction Pressure (1.7): {enforcer.calculate_correction_pressure(1.7):.3f}")

