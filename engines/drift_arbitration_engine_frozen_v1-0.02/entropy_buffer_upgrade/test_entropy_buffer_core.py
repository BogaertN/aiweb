# test_entropy_buffer_core.py

from entropy_buffer_core import EntropyBuffer

def test_entropy_buffer_behavior():
    eb = EntropyBuffer(threshold=0.1)
    eb.add_entropy_sample(0.05)
    eb.add_entropy_sample(0.15)
    assert eb.smoothed_entropy > 0, "Smoothed entropy should not be zero."
    assert isinstance(eb.needs_arbitration(), bool), "Arbitration decision must return boolean."

if __name__ == "__main__":
    test_entropy_buffer_behavior()
    print("✅ Entropy Buffer Upgrade Test Passed.")
