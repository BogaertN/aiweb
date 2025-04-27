from run import enforce_tier

print("🔹 TEST 1: Tier 1 (human)")
text1 = "This tool helps you stay calm, organize your thoughts, and journal clearly."
print(enforce_tier(text1))

print("\n🔹 TEST 2: Tier 2 (system)")
text2 = "The phase engine triggers χ(t) when symbolic recursion breaks coherence."
print(enforce_tier(text2))

print("\n🔹 TEST 3: Mixed content (violation)")
text3 = "This gentle app keeps you calm while monitoring ψ and memory stack integrity."
print(enforce_tier(text3))
