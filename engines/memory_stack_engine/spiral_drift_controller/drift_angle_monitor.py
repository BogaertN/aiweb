# drift_angle_monitor.py
# Measures angular drift in recursion breathing cycles

import math

class DriftAngleMonitor:
    def __init__(self):
        self.previous_vector = (1, 0)

    def calculate_drift_angle(self, new_vector):
        x1, y1 = self.previous_vector
        x2, y2 = new_vector

        dot = x1 * x2 + y1 * y2
        mag1 = math.hypot(x1, y1)
        mag2 = math.hypot(x2, y2)

        if mag1 == 0 or mag2 == 0:
            return 0.0

        cos_theta = dot / (mag1 * mag2)
        cos_theta = max(min(cos_theta, 1), -1)
        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)

        self.previous_vector = new_vector
        return angle_deg

if __name__ == "__main__":
    monitor = DriftAngleMonitor()
    print(f"[TEST] Drift Angle: {monitor.calculate_drift_angle((0, 1)):.2f} degrees")

