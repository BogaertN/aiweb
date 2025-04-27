from log_event import log_event

print("🔹 Logging INFO event...")
log_event("test_harness", "System test started", status="info")

print("🔹 Logging WARNING event...")
log_event("tier_enforcer", "Mixed-tier output flagged", status="warning")

print("🔹 Logging ERROR event...")
log_event("plugin_engine", "Failed to load symbolic capacitor", status="error")

print("\n📄 test_log.txt output:")
with open("test_log.txt", "r") as f:
    print(f.read())

print("📄 event_log.jsonl entries:")
with open("event_log.jsonl", "r") as f:
    for line in f:
        print(line.strip())
