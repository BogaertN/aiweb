# test_drift_correction_core.py
# Testing Gilligan Drift Correction Upgrade

from drift_correction_core import GilliganAgent

def run_test():
    agent = GilliganAgent()
    agent.symbolic_breathe()
    agent.phase_summary()
    print("✅ Gilligan Drift Correction Test Passed.")

if __name__ == "__main__":
    run_test()
