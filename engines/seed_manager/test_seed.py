from seed_core import generate_seed

def test_seed_generation():
    try:
        seed = generate_seed()
        assert "seed_id" in seed
        assert seed["status"] == "active"
        print("✅ Test Passed: Seed created successfully.")
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_seed_generation()
