# memory_stack_stack_loader.py
print("\n🌀 [MEMORY STACK] Breathing up memory stack engines...\n")

try:
    from engines.memory_stack_engine_breathing_v1.memory_breather import start_memory_breather
    start_memory_breather()
    print("\n✅ Memory Breather running.\n")
except Exception as e:
    print(f"❌ Failed to start Memory Breather: {e}")

print("✅ [MEMORY STACK] Memory Stack Breathing Complete.\n")
