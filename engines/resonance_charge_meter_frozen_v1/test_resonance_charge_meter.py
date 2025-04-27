# test_resonance_charge_meter.py
# Tests the resonance charge measurement

from run import ResonanceChargeMeter

def run_test():
    try:
        meter = ResonanceChargeMeter()
        for _ in range(2):
            meter.measure_charge()
        meter.charge_summary()
        print("✅ Resonance Charge Meter Test Passed.")
    except Exception as e:
        print(f"❌ Resonance Charge Meter Test Failed: {e}")

if __name__ == "__main__":
    run_test()

