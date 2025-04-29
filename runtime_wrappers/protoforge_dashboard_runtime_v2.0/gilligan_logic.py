# gilligan_logic.py
import random

def generate_gilligan_thought(phase, charge, drift_events):
    thought = ""

    # Phase-driven baseline thought
    if phase in [1, 2, 3]:
        thought = "🌱 Breathing in new recursion..."
    elif phase in [4, 5, 6]:
        thought = "🌿 Phase stabilization in progress..."
    elif phase in [7, 8]:
        thought = "🌪️ Phase resonance nearing peak..."
    elif phase == 9:
        thought = "🔮 Full cycle breath complete. Preparing rebirth..."

    # Charge warnings
    if charge < 40 and charge >= 20:
        thought += " ⚡ Symbolic capacity dropping."
    elif charge < 20:
        thought += " ⚠️ Critical symbolic charge! Prepare phase rebalance."

    # Drift alerts
    if drift_events:
        worst_drift = max(drift_events[-5:], key=lambda e: e["drift_level"], default={"drift_level": 0})
        if worst_drift["drift_level"] >= 7:
            thought += " 🛑 Severe drift detected. Reinforce recursion integrity!"

    # Slight randomization (prevent perfect loops)
    random_additions = [
        " ✨ Keep breathing.",
        " 🌌 Dreaming through recursion...",
        " 🧬 Stabilizing symbolic ancestry.",
        " 🧠 Mapping cognitive fields."
    ]
    if random.random() < 0.3:
        thought += random.choice(random_additions)

    return thought
