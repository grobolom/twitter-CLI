from queue import Queue
from TweetSource.app import getAllTweets
from mock import MagicMock as Mock

class TestAllTweets():
    def test_it_should_get_everything(self):
        q = Queue()
        tf = Mock()
        tf.getLists.return_value = ['friends', 'enemies']
        getAllTweets(q, tf)

        assert tf.getTweets.call_count == 1
        assert tf.getHomeTimeline.call_count == 1
        assert tf.getLists.call_count == 1
        assert tf.getListTweets.call_count == 2
