from agent_kernel_core import pulse_heartbeat

def test_kernel_heartbeat():
    try:
        result = pulse_heartbeat()
        assert result["heartbeat"] == True
        assert result["loop_phase"] == "stable"
        print("✅ Test Passed: Recursive heartbeat recorded successfully.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_kernel_heartbeat()
