# test_glyph_ui_overlay_core.py

from glyph_ui_overlay_core import GlyphUIOverlay

def test_glyph_ui_overlay_behavior():
    overlay = GlyphUIOverlay()
    glyph = overlay.render_glyph("GLYPH-TEST", "Φ3")
    assert glyph["glyph_id"] == "GLYPH-TEST", "Glyph ID must match."
    assert glyph["phase_origin"] == "Φ3", "Phase origin must match."
    print("✅ Glyph UI Overlay Test Passed.")

if __name__ == "__main__":
    test_glyph_ui_overlay_behavior()
