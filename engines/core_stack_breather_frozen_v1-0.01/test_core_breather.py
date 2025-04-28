# test_core_breather.py

from core_breather import CoreBreather

def test_breath_cycle():
    breather = CoreBreather()
    for _ in range(18):  # Two full cycles
        breather.breathe()
    print("✅ Core Stack Breath Cycle Test Passed")

if __name__ == "__main__":
    test_breath_cycle()
