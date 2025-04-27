# external_feed_core.py
# External Feed Listener Core

class ExternalFeedListener:
    def __init__(self):
        self.feeds = []

    def receive_feed(self, feed_name, feed_data):
        feed_record = {
            "feed_name": feed_name,
            "feed_data": feed_data
        }
        self.feeds.append(feed_record)
        return feed_record

if __name__ == "__main__":
    listener = ExternalFeedListener()
    record = listener.receive_feed("external_signal_1", {"value": 42})
    print(f"[TEST] Feed Received: {record}")
