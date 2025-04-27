# entropy_monitor_core.py
# Entropy Monitor Core

class EntropyMonitor:
    def __init__(self):
        self.entropy_readings = []

    def record_entropy(self, value):
        self.entropy_readings.append(value)

    def average_entropy(self):
        if not self.entropy_readings:
            return 0
        return sum(self.entropy_readings) / len(self.entropy_readings)

if __name__ == "__main__":
    monitor = EntropyMonitor()
    monitor.record_entropy(0.25)
    monitor.record_entropy(0.30)
    print(f"[TEST] Average Entropy: {monitor.average_entropy()}")
