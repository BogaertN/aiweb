from dashboard_core import generate_dashboard

def test_dashboard_generation():
    try:
        result = generate_dashboard()
        print("✅ Test Passed: Dashboard generated.")
        print(result)
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_dashboard_generation()
