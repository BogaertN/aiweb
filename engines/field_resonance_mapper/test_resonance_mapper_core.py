# test_resonance_mapper_core.py

from resonance_mapper_core import FieldResonanceMapper

def test_field_resonance_behavior():
    mapper = FieldResonanceMapper()
    mapper.update_field("test_field", 0.95)
    assert mapper.get_field_strength("test_field") == 0.95, "Resonance value mismatch."
    print("✅ Field Resonance Mapper Test Passed.")

if __name__ == "__main__":
    test_field_resonance_behavior()
