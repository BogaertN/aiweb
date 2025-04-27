# glyph_core.py
# Glyph Engine Core

class GlyphEngine:
    def __init__(self):
        self.glyphs = []

    def create_glyph(self, symbol_id, phase_origin):
        glyph = {
            "symbol_id": symbol_id,
            "phase_origin": phase_origin,
            "stability_factor": 1.0,
            "ancestral_trace": []
        }
        self.glyphs.append(glyph)
        return glyph

if __name__ == "__main__":
    engine = GlyphEngine()
    glyph = engine.create_glyph("GLYPH-001", "Φ1")
    print(f"[TEST] Created Glyph: {glyph}")
