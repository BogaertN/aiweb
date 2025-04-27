from run import detect_drift
from pathlib import Path
import json

# Simulate state injection for testing
FIELD_STATE_PATH = Path("../../engines/recursive_field_engine/field_state.json").resolve()

# Test cases
test_cases = [
    {"loop_integrity": 1.0, "drift_factor": 0.0, "charge": 0.0, "last_input": "echo pass"},
    {"loop_integrity": 0.65, "drift_factor": 0.35, "charge": 0.2, "last_input": "error fail"},
    {"loop_integrity": 0.80, "drift_factor": 0.25, "charge": 0.1, "last_input": "almost"},
]

for i, state in enumerate(test_cases, 1):
    with open(FIELD_STATE_PATH, "w") as f:
        json.dump(state, f)

    print(f"\n🧪 TEST CASE {i}")
    result = detect_drift()
    print("Status:", result["status"])
    print("Input:", result["input"])
