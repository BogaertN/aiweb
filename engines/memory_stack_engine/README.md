# memory_stack_engine

**AI.Web Memory Persistence Engine – Symbolic Output Stack**

This engine captures symbolic output from other engines (e.g., phase transitions, tier classifications, agent messages) and appends them to a local file-based stack: `stack.json`.

It also maintains a running action log in `test_log.txt`.

---

### 🔧 Features

- `write_to_stack(data)`  
  Appends a memory entry to `stack.json` with a timestamp.

- `read_stack()`  
  Returns the full memory trail for review or external access.

- `_log()`  
  Writes all internal actions to `test_log.txt` for audit or replay.

---

### 📂 Files

- `log.py` — core logic (write + read memory)
- `stack.json` — live symbolic memory stack (auto-created)
- `test_log.txt` — action + error trace for all stack activity
- `engine_manifest.json` — version-locked metadata
- `__init__.py` — marks this folder as a Python module

---

### 🚫 Edit Policy

This engine is considered frozen once versioned.

If changes are needed:
- Fork into `memory_stack_engine_v2/`
- Update the manifest version
- Re-test with the system harness

