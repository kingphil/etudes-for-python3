import unittest

# note: the page numbers refer to "Python Pocket Reference, Mark Lutz, 5th edition"

class TestGenerator(unittest.TestCase):
    def test_expression_basic(self):
        # generator expressions: p 51
        # note: ~18 quintillion, for IPv6 fans
        #   if this were a list comprehension, it would likely consume all memory
        nums = (x for x in range(2**64))
        for x in range(2**8):
            # throw away the first 256
            next(nums)
        self.assertEqual(next(nums), 256, "generator expression")

    def _generator_function(self):
        for x in range(2**64):
            sent = yield(x)
            if sent:
                yield(x-100)

    def test_function_basic(self):
        gen_func = self._generator_function()
        for x in range(2**8):
            next(gen_func)
        self.assertEqual(next(gen_func), 256, "generator function")

    def test_function_with_send(self):
        gen_func = self._generator_function()
        for x in range(2**8):
            next(gen_func)
        # what an odd construct; not certain when I would ever use .send(...)
        # note: the function as written, x is 255 twice; we distinguish it by subtraction
        rv = gen_func.send("pek")
        self.assertEqual(rv, 155, "generator function with send")
        # p 87 (paraphrasing) if next() is called, yield returns None <--- seemingly not correct
        rv = next(gen_func)
        self.assertTrue(rv is not None, "generator function with send")
        self.assertEqual(rv, 256, "generator function with send")
