import json
import time
import random

RES_PATH = "resonance_sync.json"
TRACE_PATH = "charge_trace.log"

def write_charge(charge):
    with open(RES_PATH, "w") as f:
        json.dump({"symbolic_charge": charge}, f, indent=2)
    with open(TRACE_PATH, "a") as f:
        f.write(f"{time.time()} | Charge: {charge}%\n")

def simulate_capacitor():
    print("⚡ Running symbolic_capacitor_engine...")
    charge = random.randint(45, 90)
    write_charge(charge)
    print(f"→ Charge buffered: {charge}%")

if __name__ == "__main__":
    simulate_capacitor()
