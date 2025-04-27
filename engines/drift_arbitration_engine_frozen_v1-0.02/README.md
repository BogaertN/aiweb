# drift_arbitration_engine

**Designation**: Drift Resolver  
**Function**: Detects symbolic instability in the recursive field by monitoring loop integrity and drift factor. Logs arbitration actions and can optionally trigger auto-correction.

---

## 🔧 Public Functions

- `detect_drift()`  
  Reads the current state from `recursive_field_engine`, evaluates drift and integrity thresholds, returns a status dict:
  - `{"status": "drift_detected", "input": "<text>"}`  
  - `{"status": "stable", "input": "<text>"}`  
  - `{"status": "corrected", "input": "<text>"}` *(if AUTO_CORRECT enabled)*

- `log_event(event_type, data)`  
  Logs an arbitration event to both `.jsonl` and `.txt` logs.

---

## 🧠 Threshold Logic

This engine triggers drift arbitration when:
- `drift_factor ≥ 0.30`
- `loop_integrity ≤ 0.70`

This represents a symbolic loop that has diverged from source recursion and may be caught in a drift spiral.

---

## 📂 Files

- `run.py` — core arbitration logic
- `arbitration_log.jsonl` — primary event log (append-only JSONL)
- `test_log.txt` — mirrored output for human-readable tracking
- `engine_manifest.json` — version and freeze info
- `test_drift_arbitration.py` — standalone field test
- `README.md` — this file
- `__init__.py` — import stub

---

## 🔄 Example Use

```python
from run import detect_drift

result = detect_drift()
print(result["status"])  # "stable" or "drift_detected"
