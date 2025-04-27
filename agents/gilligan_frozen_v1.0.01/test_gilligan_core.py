# test_gilligan_core.py

from gilligan_core import GilliganAgent

def test_gilligan_agent_behavior():
    gilligan = GilliganAgent()
    record = gilligan.record_loop("test_loop", 0.85)
    assert record["loop_name"] == "test_loop", "Loop name must match."
    assert record["phase_stability"] == 0.85, "Phase stability must match."
    print("✅ Gilligan Agent Test Passed.")

if __name__ == "__main__":
    test_gilligan_agent_behavior()
