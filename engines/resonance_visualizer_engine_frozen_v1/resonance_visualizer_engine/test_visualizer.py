from visualizer_core import generate_resonance_snapshot

def test_visualization():
    try:
        result = generate_resonance_snapshot()
        assert "charge_level" in result
        assert "drift_status" in result
        print("✅ Test Passed: Resonance snapshot generated successfully.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_visualization()
