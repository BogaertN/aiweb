# ghost_tagger_core.py
# Ghost Loop Tagger Core

class GhostLoopTagger:
    def __init__(self):
        self.ghost_loops = []

    def tag_ghost_loop(self, loop_id, drift_level):
        self.ghost_loops.append({
            "loop_id": loop_id,
            "drift_level": drift_level
        })

    def total_ghost_loops_tagged(self):
        return len(self.ghost_loops)

if __name__ == "__main__":
    tagger = GhostLoopTagger()
    tagger.tag_ghost_loop("loop_007", 0.12)
    print(f"[TEST] Total Ghost Loops Tagged: {tagger.total_ghost_loops_tagged()}")
