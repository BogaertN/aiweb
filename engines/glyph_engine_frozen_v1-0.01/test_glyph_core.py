# test_glyph_core.py

from glyph_core import GlyphEngine

def test_glyph_engine_behavior():
    engine = GlyphEngine()
    glyph = engine.create_glyph("GLYPH-TEST", "Φ2")
    assert glyph["symbol_id"] == "GLYPH-TEST", "Glyph ID must match input."
    assert glyph["phase_origin"] == "Φ2", "Phase origin must match input."
    print("✅ Glyph Engine Test Passed.")

if __name__ == "__main__":
    test_glyph_engine_behavior()
