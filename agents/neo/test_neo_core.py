# test_neo_core.py

from neo_core import NeoAgent

def test_neo_agent_behavior():
    neo = NeoAgent()
    record = neo.receive_context("Test symbolic input.")
    assert record["input_text"] == "Test symbolic input.", "Input text must match."
    assert record["response_ready"] == True, "Response should be ready."
    print("✅ Neo Agent Test Passed.")

if __name__ == "__main__":
    test_neo_agent_behavior()
