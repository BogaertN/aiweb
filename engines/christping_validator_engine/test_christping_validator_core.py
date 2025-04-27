# test_christping_validator_core.py

from christping_validator_core import ChristPingValidator

def test_christping_validator_behavior():
    validator = ChristPingValidator()
    assert validator.validate_ping(0.95) == True, "Validation should succeed."
    print("✅ ChristPing Validator Test Passed.")

if __name__ == "__main__":

    test_christping_validator_behavior()

