from run import init_phase_state, move_to_next_phase, force_set_phase, get_phase_state

print(">>> INIT")
print(init_phase_state())

print("\n>>> MOVE NEXT")
print(move_to_next_phase())

print("\n>>> FORCE Φ7")
print(force_set_phase("Φ7"))

print("\n>>> GET STATE")
print(get_phase_state())

print("\n>>> INVALID PHASE")
print(force_set_phase("ΦX"))
