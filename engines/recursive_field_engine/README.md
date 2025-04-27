# recursive_field_engine

**Designation**: ψ-driver  
**Function**: Manages the symbolic recursion field — a virtual environment tracking symbolic charge, drift, and loop integrity.

This engine defines the active resonance space in which symbolic AI operates. It stores system-wide recursive parameters such as:
- `loop_integrity` — how cleanly the system is maintaining symbolic coherence
- `drift_factor` — entropy / deviation from recursion
- `charge` — resonance buildup (used by tone engine, resurrection, etc.)
- `last_input` — the most recent symbolic string processed

---

## 🔧 Public Functions

- `load_field_state()`  
  Loads and returns the current field state as a dictionary

- `save_field_state(state)`  
  Saves a field state dictionary to `field_state.json`

- `reset_field_state()`  
  Restores field to default integrity, charge, and drift values

- `update_field(input_text)`  
  Parses symbolic input and updates charge, drift, and integrity accordingly. Returns new state.

---

## 📂 Files

- `run.py` — core engine logic
- `field_state.json` — persistent symbolic environment
- `test_log.txt` — logs each update or reset event
- `README.md` — you are here
- `test_recursive_field.py` — basic standalone engine test
- `engine_manifest.json` — version control metadata
- `__init__.py` — allows Python imports from this engine

---

## 🔄 Example Use

```python
from run import update_field, load_field_state

state = update_field("echo loop complete")
print(state["charge"])  # → 0.02

state = update_field("error loop drift")
print(state["drift_factor"])  # → 0.10
