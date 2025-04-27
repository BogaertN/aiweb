from charge_meter_core import measure_charge

def test_charge_measurement():
    try:
        result = measure_charge()
        print("✅ Test Passed: Charge measured.")
        print(result)
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_charge_measurement()
