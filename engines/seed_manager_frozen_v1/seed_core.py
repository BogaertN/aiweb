import json
import uuid
import datetime

SEED_STORAGE = "seed_bank.json"

def generate_seed(seed_type="symbolic_memory"):
    seed = {
        "seed_id": str(uuid.uuid4()),
        "type": seed_type,
        "created_at": datetime.datetime.utcnow().isoformat() + "Z",
        "status": "active"
    }
    try:
        try:
            with open(SEED_STORAGE, "r") as f:
                seeds = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            seeds = []

        seeds.append(seed)

        with open(SEED_STORAGE, "w") as f:
            json.dump(seeds, f, indent=2)

        print(f"✔️ New symbolic seed generated: {seed}")
        return seed
    except Exception as e:
        print(f"[!] Failed to generate seed: {e}")
        return None
