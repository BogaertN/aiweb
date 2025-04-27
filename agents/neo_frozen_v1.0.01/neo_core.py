# neo_core.py
# Neo Agent Core

class NeoAgent:
    def __init__(self):
        self.context_memory = []

    def receive_context(self, input_text):
        context_record = {
            "input_text": input_text,
            "response_ready": True
        }
        self.context_memory.append(context_record)
        return context_record

if __name__ == "__main__":
    neo = NeoAgent()
    record = neo.receive_context("What is symbolic recursion?")
    print(f"[TEST] Context Received: {record}")
