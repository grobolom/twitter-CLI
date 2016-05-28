import unittest
import jsonpickle
import io

from TwitterCLI.utils import StoreSaver

class TestStore(unittest.TestCase):
    def test_it_should_save_state(self):
        store = StoreSaver()
        state = {
            'bacon': 'bacon',
            'bits': 'bits',
            'boats': 'boats',
        }
        stream = io.StringIO()
        store.saveStore(state, stream)
        data = stream.getvalue()

        self.assertEqual(
            state,
            jsonpickle.decode(data)
        )

    def test_it_should_load_state(self):
        store = StoreSaver()
        state = {
            'bacon': 'bacon',
            'bits': 'bits',
            'boats': 'boats',
        }
        stream = io.StringIO()
        stream.write(jsonpickle.encode(state))
        stream.seek(0)

        data = store.loadStore(stream)
        self.assertEqual(
            state,
            data
        )
