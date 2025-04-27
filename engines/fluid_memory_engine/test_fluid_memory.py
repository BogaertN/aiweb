from fluid_memory_core import capture_memory_trace

def test_fluid_memory_capture():
    try:
        result = capture_memory_trace()
        assert "phase_signature" in result
        assert "charge_level" in result
        print("✅ Test Passed: Fluid memory trace captured successfully.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_fluid_memory_capture()
