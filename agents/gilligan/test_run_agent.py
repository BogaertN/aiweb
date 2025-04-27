# test_run_agent.py
# Test breathing for Gilligan

from run import GilliganAgent

if __name__ == "__main__":
    agent = GilliganAgent()
    agent.symbolic_breathe()
    agent.phase_summary()
    print("✅ Gilligan Agent Test Passed.")
