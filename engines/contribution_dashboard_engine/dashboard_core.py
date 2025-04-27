import json
import os
import time

CONTRIBUTION_LOG = "../compute_contribution_engine_frozen_v1/contribution_log.jsonl"
TOKEN_LEDGER = "../awh_token_runtime_frozen_v1/token_ledger.json"
DASHBOARD_OUTPUT = "dashboard_output.json"

def generate_dashboard():
    contributions = []
    tokens = []

    # Read contribution events
    try:
        with open(CONTRIBUTION_LOG, "r") as f:
            for line in f:
                contributions.append(json.loads(line.strip()))
    except Exception as e:
        print(f"[!] Failed to read contributions: {e}")

    # Read token ledger
    try:
        with open(TOKEN_LEDGER, "r") as f:
            tokens = json.load(f)
    except Exception as e:
        print(f"[!] Failed to read tokens: {e}")

    dashboard = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total_contributions": len(contributions),
        "total_tokens_earned": sum(entry.get("tokens_earned", 0) for entry in tokens),
        "recent_contributors": [c.get("contributor_id", "unknown") for c in contributions[-5:]]
    }

    try:
        with open(DASHBOARD_OUTPUT, "w") as f:
            json.dump(dashboard, f, indent=2)
        print(f"✔️ Dashboard generated: {dashboard}")
    except Exception as e:
        print(f"[!] Failed to write dashboard output: {e}")

    return dashboard
