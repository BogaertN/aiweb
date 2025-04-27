# test_drift_analyzer_core.py

from drift_analyzer_core import DriftAnalyzerTool

def test_drift_analyzer_behavior():
    analyzer = DriftAnalyzerTool()
    record = analyzer.analyze_drift("test_field", 0.2)
    assert record["field_id"] == "test_field", "Field ID must match."
    assert record["drift_amount"] == 0.2, "Drift amount must match."
    print("✅ Drift Analyzer Tool Test Passed.")

if __name__ == "__main__":
    test_drift_analyzer_behavior()
