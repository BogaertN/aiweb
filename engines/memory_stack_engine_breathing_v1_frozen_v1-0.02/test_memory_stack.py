from log import write_to_stack, read_stack

print("🔹 Writing memory entry #1...")
write_to_stack({"source": "test", "event": "init"})

print("🔹 Writing memory entry #2...")
write_to_stack({"source": "test", "event": "phase_step", "phase": "Φ4"})

print("\n🔍 Reading stack...")
stack = read_stack()
for i, entry in enumerate(stack, 1):
    print(f"{i}: {entry}")
