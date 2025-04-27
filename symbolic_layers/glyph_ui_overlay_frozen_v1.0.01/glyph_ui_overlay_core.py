# glyph_ui_overlay_core.py
# Glyph UI Overlay Core

class GlyphUIOverlay:
    def __init__(self):
        self.displayed_glyphs = []

    def render_glyph(self, glyph_id, phase_origin):
        glyph_display = {
            "glyph_id": glyph_id,
            "phase_origin": phase_origin
        }
        self.displayed_glyphs.append(glyph_display)
        return glyph_display

if __name__ == "__main__":
    overlay = GlyphUIOverlay()
    glyph = overlay.render_glyph("GLYPH-007", "Φ6")
    print(f"[TEST] Glyph Rendered: {glyph}")
