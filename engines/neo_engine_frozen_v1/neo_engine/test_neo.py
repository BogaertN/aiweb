from neo_core import generate_symbolic_response

def test_neo_response():
    try:
        result = generate_symbolic_response()
        assert "tone" in result
        assert "message" in result
        print("✅ Test Passed: Neo generated a symbolic response.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_neo_response()
