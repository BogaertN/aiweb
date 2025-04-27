# field_feed_core.py
# Phase 1.5 External Field Feed Adapter Upgrade

class ExternalFieldFeedAdapter:
    def __init__(self):
        self.external_feeds = []

    def attach_feed(self, feed_source):
        self.external_feeds.append(feed_source)

    def feed_count(self):
        return len(self.external_feeds)

if __name__ == "__main__":
    adapter = ExternalFieldFeedAdapter()
    adapter.attach_feed("external_sensor_A")
    print(f"[TEST] External Feeds Attached: {adapter.feed_count()}")
