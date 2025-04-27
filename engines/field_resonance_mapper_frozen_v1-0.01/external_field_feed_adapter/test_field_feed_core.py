# test_field_feed_core.py

from field_feed_core import ExternalFieldFeedAdapter

def test_external_field_feed_behavior():
    adapter = ExternalFieldFeedAdapter()
    adapter.attach_feed("test_sensor")
    assert adapter.feed_count() == 1, "Feed count mismatch."
    print("✅ External Field Feed Adapter Test Passed.")

if __name__ == "__main__":
    test_external_field_feed_behavior()
