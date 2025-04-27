# test_entropy_monitor_core.py

from entropy_monitor_core import EntropyMonitor

def test_entropy_monitor_behavior():
    monitor = EntropyMonitor()
    monitor.record_entropy(0.25)
    monitor.record_entropy(0.30)
    avg = monitor.average_entropy()
    assert avg > 0, "Average entropy should be greater than zero."
    print("✅ Entropy Monitor Test Passed.")

if __name__ == "__main__":
    test_entropy_monitor_behavior()
