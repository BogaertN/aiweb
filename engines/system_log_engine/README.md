# system_log_engine

**AI.Web System Log Engine – Global Runtime Event Logger**

This engine captures system-wide events and writes them to a persistent JSONL stream. It is used for:

- Phase updates
- Plugin load messages
- Tier enforcement flags
- User or agent-triggered logs
- Drift warnings and symbolic errors

All events are mirrored to `test_log.txt` for local debugging.

---

### 🔧 Features

- `log_event(source, message, status="info")`  
  Appends an event entry with timestamp, source, status, and message.

- Output stream:  
  `event_log.jsonl` — one JSON object per line (newline-delimited format for tailing, replaying, or parsing)

- Mirror file:  
  `test_log.txt` — simplified log for dev console review

---

### 🧩 Example Use

```python
log_event("phase_engine", "Entered Φ6", status="info")
log_event("tier_enforcer", "Mixed tier output blocked", status="warning")
log_event("plugin_loader", "Failed to load `drift_watchdog`", status="error")
