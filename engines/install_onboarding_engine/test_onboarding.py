from onboarding_core import setup_environment

def test_install_setup():
    try:
        result = setup_environment()
        print("✅ Test Passed: Install environment checked.")
        print("Install Report:", result)
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_install_setup()
