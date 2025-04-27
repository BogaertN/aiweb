import json
import time
import random

LOG_FILE = "peer_comm_log.jsonl"

def simulate_peer_message():
    peer_id = f"peer_{random.randint(1000,9999)}"
    message_type = random.choice(["status_update", "sync_request", "handshake_ack"])
    symbolic_charge = random.randint(20, 100)

    message = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "peer_id": peer_id,
        "type": message_type,
        "charge_level": symbolic_charge
    }

    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(message) + "\n")
        print(f"✔️ Sent simulated peer message: {message}")
    except Exception as e:
        print(f"[!] Failed to log peer message: {e}")

    return message
