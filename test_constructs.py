import unittest

# note: the page numbers refer to "Python Pocket Reference, Mark Lutz, 5th edition"

class TestGenerator(unittest.TestCase):
    def test_expression_basic(self):
        # generator expressions: p 51
        # note: ~18 quintillion, for IPv6 fans; if this were a list comprehension, it would
        #   likely consume all of your memory
        nums = (x for x in range(2**64))
        for x in range(2**8):
            # throw away the first 256
            next(nums)
        self.assertEqual(next(nums), 256, "generator expression")
