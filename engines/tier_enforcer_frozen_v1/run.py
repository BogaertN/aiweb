# run.py – AI.Web Tier Enforcer
# Enforces Tier 1 (human-facing) and Tier 2 (system-level) output separation

import json
from datetime import datetime
from pathlib import Path

# File paths
RULES_FILE = Path(__file__).parent / "tier_rules.json"
VIOLATION_LOG = Path(__file__).parent / "tier_violation_log.json"
TEST_LOG = Path(__file__).parent / "test_log.txt"

# Load rules from tier_rules.json
def load_rules():
    if not RULES_FILE.exists():
        raise FileNotFoundError("tier_rules.json not found.")
    return json.loads(RULES_FILE.read_text())

# Basic logger
def _log_event(msg):
    with open(TEST_LOG, "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

# Log a violation
def log_violation(content, reason, detected_tier):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "reason": reason,
        "tier_detected": detected_tier,
        "content": content
    }

    # Append to log
    if VIOLATION_LOG.exists():
        log = json.loads(VIOLATION_LOG.read_text())
    else:
        log = []

    log.append(log_entry)
    VIOLATION_LOG.write_text(json.dumps(log, indent=2))

# Classify input as Tier 1, Tier 2, or MIXED
def classify_output(text):
    rules = load_rules()
    tier1_hits = sum(1 for word in rules["tier1_keywords"] if word in text.lower())
    tier2_hits = sum(1 for word in rules["tier2_keywords"] if word in text.lower())

    if tier1_hits > 0 and tier2_hits > 0:
        return "MIXED"
    elif tier2_hits > tier1_hits:
        return "TIER 2"
    elif tier1_hits > 0:
        return "TIER 1"
    else:
        return "UNCLASSIFIED"

# Enforce tier protocol
def enforce_tier(text):
    result = classify_output(text)
    _log_event(f"Checked content: classified as {result}")

    if result == "MIXED":
        log_violation(text, "Cross-tier contamination", result)
        return "[TIER VIOLATION] Output rejected due to mixed content."
    elif result == "TIER 1":
        return f"[TIER 1] {text}"
    elif result == "TIER 2":
        return f"[TIER 2] {text}"
    else:
        log_violation(text, "Unclassified content", result)
        return "[UNCLASSIFIED] Output does not match Tier 1 or Tier 2."

