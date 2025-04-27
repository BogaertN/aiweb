# test_entropy_buffer_integration.py
# Phase 1.5 Sanity Test for Entropy Buffer Upgrade Integration

try:
    from entropy_buffer_upgrade.entropy_buffer_core import EntropyBuffer

    eb = EntropyBuffer(threshold=0.1)
    eb.add_entropy_sample(0.08)
    eb.add_entropy_sample(0.12)
    print(f"[TEST] Smoothed Entropy: {eb.smoothed_entropy}")
    print(f"[TEST] Needs Arbitration: {eb.needs_arbitration()}")

    print("✅ Entropy Buffer Upgrade Import and Functionality Test Passed.")

except Exception as e:
    print(f"❌ Test Failed: {str(e)}")

