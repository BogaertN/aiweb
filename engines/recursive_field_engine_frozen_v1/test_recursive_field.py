from run import reset_field_state, update_field, load_field_state

print("🔄 Resetting field...")
reset_field_state()
state = load_field_state()
print("Initial state:", state)

print("\n⚡ Input: echo this loop")
state = update_field("echo this loop")
print("State after echo:", state)

print("\n🚨 Input: error loop drift")
state = update_field("error loop drift")
print("State after error:", state)

print("\n✅ Test complete")
