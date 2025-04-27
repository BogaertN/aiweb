# plugin_engine

**AI.Web Plugin Engine – Dynamic Loader for Optional Modules**

This engine scans the `~/aiweb/plugins/` directory, attempts to import any `.py` plugin files, and logs the result.

Plugins are not executed. They are only checked for valid Python structure and runtime importability.

---

### 🔧 Features

- `load_plugins()`  
  Loads all Python files in the `plugins/` directory.  
  Logs `[OK]` for successful imports, `[FAIL]` for any errors.

- Internal Log  
  - `test_log.txt` – all plugin activity is written here with timestamped entries.

- Plugin Folder  
  - All plugins must be placed in: `~/aiweb/plugins/`
  - Filenames must end in `.py` and not start with `_`.

---

### 🧪 Example Use

```python
load_plugins()
