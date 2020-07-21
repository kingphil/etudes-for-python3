import unittest
from unittest.mock import MagicMock

# https://docs.python.org/3/library/unittest.mock-examples.html
class GrokMock(unittest.TestCase):
    def test_mock_patching_methods(self):
        prod = ProductionClass()
        prod.something = MagicMock()
        prod.method()
        prod.something.assert_called_once_with(1, 2)
        self.assertFalse(prod.real_called)

    def test_mock_method_calls_on_object(self):
        prod = ProductionClass()
        some_obj = MagicMock()
        prod.closer(some_obj)
        some_obj.close.assert_called_once_with()

class ProductionClass:
    def __init__(self):
        self.real_called = False
    def method(self):
        # note: MagicMock does not detect that this is called w/wrong arguments...
        self.something(1, 2)
    def something(self, a, b, c):
        self.real_called = True
        return 1234
    def closer(self, something):
        # note: 'some_obj' above does not really have a 'close' method
        something.close()
