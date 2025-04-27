
from tone_core import update_tone_state

def test_tone_update():
    try:
        result = update_tone_state()
        print("✅ Test Passed: Tone updated.")
        print(result)
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_tone_update()
