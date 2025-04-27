# test_ghost_tagger_core.py

from ghost_tagger_core import GhostLoopTagger

def test_ghost_loop_tagger_behavior():
    tagger = GhostLoopTagger()
    tagger.tag_ghost_loop("loop_test", 0.1)
    assert tagger.total_ghost_loops_tagged() == 1, "Should tag one ghost loop."
    print("✅ Ghost Loop Tagger Test Passed.")

if __name__ == "__main__":
    test_ghost_loop_tagger_behavior()
