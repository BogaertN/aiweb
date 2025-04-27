# test_glyph_core.py

from glyph_core import generate_glyph

def test_generate_glyph():
    glyph = generate_glyph()
    assert "symbol_id" in glyph
    assert "phase_origin" in glyph
    print("✅ Symbolic Glyph Generation Test Passed")

if __name__ == "__main__":
    test_generate_glyph()
