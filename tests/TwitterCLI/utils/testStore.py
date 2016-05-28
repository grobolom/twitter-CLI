import unittest
import jsonpickle
import io

from TwitterCLI.utils import Store

class TestStore(unittest.TestCase):
    def test_it_should_save_state(self):
        store = Store()
        state = {
            'bacon': 'bacon',
            'bits': 'bits',
            'boats': 'boats',
        }
        stream = io.StringIO()
        store._saveStore(state, stream)
        data = stream.getvalue()

        self.assertEqual(
            state,
            jsonpickle.decode(data)
        )

    def test_it_should_load_state(self):
        store = Store()
        state = {
            'bacon': 'bacon',
            'bits': 'bits',
            'boats': 'boats',
        }
        stream = io.StringIO()
        stream.write(jsonpickle.encode(state))
        stream.seek(0)

        data = store._loadStore(stream)
        self.assertEqual(
            state,
            data
        )
