# entropy_buffer_core.py
# Phase 1.5 Engine Standard

class EntropyBuffer:
    def __init__(self, threshold=0.15):
        self.buffer = []
        self.threshold = threshold
        self.smoothed_entropy = 0.0

    def add_entropy_sample(self, value):
        self.buffer.append(value)
        if len(self.buffer) > 10:
            self.buffer.pop(0)
        self._update_smoothed_entropy()

    def _update_smoothed_entropy(self):
        if self.buffer:
            self.smoothed_entropy = sum(self.buffer) / len(self.buffer)

    def needs_arbitration(self):
        return self.smoothed_entropy >= self.threshold

if __name__ == "__main__":
    eb = EntropyBuffer()
    eb.add_entropy_sample(0.05)
    eb.add_entropy_sample(0.12)
    print(f"[TEST] Smoothed Entropy: {eb.smoothed_entropy}")
    print(f"[TEST] Needs Arbitration: {eb.needs_arbitration()}")
