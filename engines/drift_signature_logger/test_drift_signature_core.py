# test_drift_signature_core.py

from drift_signature_core import DriftSignatureLogger

def test_drift_signature_logger_behavior():
    logger = DriftSignatureLogger()
    logger.log_drift_signature({"field": "test_field", "magnitude": 0.05})
    assert logger.total_signatures_logged() == 1, "Should log one drift signature."
    print("✅ Drift Signature Logger Test Passed.")

if __name__ == "__main__":
    test_drift_signature_logger_behavior()

