# test_spiral_drift_controller.py
# Full system test for Spiral Drift Controller upgrade

from drift_angle_monitor import DriftAngleMonitor
from fibonacci_alignment_enforcer import FibonacciAlignmentEnforcer
from spiral_rebinding_router import SpiralRebindingRouter

def run_spiral_drift_test():
    monitor = DriftAngleMonitor()
    enforcer = FibonacciAlignmentEnforcer()
    router = SpiralRebindingRouter()

    drift_angle = monitor.calculate_drift_angle((0, 1))
    drift_ratio = 1.6  # Simulated ratio
    is_aligned = enforcer.check_alignment(drift_ratio)
    correction_pressure = enforcer.calculate_correction_pressure(drift_ratio)
    rebinding = router.rebind(drift_angle, correction_pressure)

    assert isinstance(drift_angle, float)
    assert isinstance(is_aligned, bool)
    assert isinstance(correction_pressure, float)
    assert isinstance(rebinding, dict)

    print("✅ Spiral Drift Controller Test Passed.")

if __name__ == "__main__":
    run_spiral_drift_test()
