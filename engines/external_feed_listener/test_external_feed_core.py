# test_external_feed_core.py

from external_feed_core import ExternalFeedListener

def test_external_feed_listener_behavior():
    listener = ExternalFeedListener()
    record = listener.receive_feed("test_feed", {"signal": 99})
    assert record["feed_name"] == "test_feed", "Feed name should match."
    assert record["feed_data"]["signal"] == 99, "Feed data should match."
    print("✅ External Feed Listener Test Passed.")

if __name__ == "__main__":
    test_external_feed_listener_behavior()
