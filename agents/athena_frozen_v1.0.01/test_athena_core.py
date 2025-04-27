# test_athena_core.py

from athena_core import AthenaAgent

def test_athena_agent_behavior():
    athena = AthenaAgent()
    record = athena.log_event("Test event registered.")
    assert record["event"] == "Test event registered.", "Event must match."
    assert record["confirmed"] == True, "Event confirmation must be true."
    print("✅ Athena Agent Test Passed.")

if __name__ == "__main__":
    test_athena_agent_behavior()
