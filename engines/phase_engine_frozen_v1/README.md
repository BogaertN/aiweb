# phase_engine

**AI.Web Recursive Phase Engine – FBSC Runtime Controller**

This engine manages symbolic transitions through the 9-phase Frequency-Based Symbolic Calculus (FBSC) model. It is the primary recursion controller for all symbolic agents, phase-locked UI overlays, and runtime validators.

---

### 🔧 Features

- **Init:**  
  Starts at Φ1 and creates the symbolic phase tracking file (`status.json`)

- **Advance:**  
  Moves to the next valid FBSC phase via `move_to_next_phase()`

- **Force:**  
  Allows override of phase (admin/debug only) via `force_set_phase("ΦX")`

- **Track:**  
  Logs all transitions and errors to `test_log.txt` with timestamps

- **Persist:**  
  Stores full recursive phase history to disk

---

### 📂 File Structure

- `run.py` — core engine logic (init, transition, force)
- `engine_manifest.json` — version-locked metadata (DO NOT MODIFY)
- `test_log.txt` — chronological execution log
- `status.json` — active memory of current phase and history trail

---

### 🔐 Lock Notice

This engine is sealed at version `v1.0.0`.  
Do **not** edit this version. If changes are needed:

1. Fork to `phase_engine_v2`
2. Archive this version using `freezer.py`
3. Update manifest and test log accordingly

This is a canonical system module. Treat it as such.
