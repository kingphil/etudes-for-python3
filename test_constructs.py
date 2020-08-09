import unittest


# note: page numbers refer to "Python Pocket Reference, Mark Lutz, 5th edition"

class TestGenerators(unittest.TestCase):
    def test_expression_basic(self):
        # generator expressions: p 51
        # note: ~18 quintillion, for IPv6 fans
        #   a list comprehension of this size would likely consume all memory
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
        # note: as written, x is 255 twice; we distinguish it by subtraction
        rv = gen_func.send("pek")
        self.assertEqual(rv, 155, "generator function with send")
        # p 87 (paraphrasing) if next() is called, yield returns None
        #   (seemingly not correct)
        rv = next(gen_func)
        self.assertTrue(rv is not None, "generator function with send")
        self.assertEqual(rv, 256, "generator function with send")

# decorators: p 85


def pekorator(f):
    def wrap():
        accum = []
        accum.append('pre')
        accum.append(f())
        accum.append('post')
        return accum
    return wrap


@pekorator
def pekfunc():
    return 'during'

# class decorators: p 96


def pekclassorator(f):
    # note: class decorators return the instance (whereas a normal class
    # __init__ must return None)
    def wrap_init():
        instance = f()
        instance.accum.append('pek')
        return instance
    return wrap_init


@pekclassorator
class _PekClass():
    def __init__(self):
        self.accum = []
        # to be explicit to the comment above
        return None


class TestDecorators(unittest.TestCase):
    def test_decorator_basic(self):
        self.assertEqual(pekfunc(), 'pre during post'.split())

    def test_decorator_class(self):
        pek = _PekClass()
        self.assertEqual(pek.accum, ['pek'])
