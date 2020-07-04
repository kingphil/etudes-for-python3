# python3 -m unittest [-v]
# python3 -m unittest test_grok_unittest[.py] [-v]
# python3 -m unittest -k <pattern>
# python3 -m unittest discover -s <directory>

# elpy: C-c C-c, then:
# unittest.main()

import unittest
import sys


# assertEqual, assertNotEqual, assertTrue, assertFalse
# assertRaises, fail
class TestGrokUnitTest(unittest.TestCase):
    def setUp(self):
        self.thingy = PekObj()

    def tearDown(self):
        pass

    def test_basic_functionality(self):
        self.assertEqual(self.thingy.echo('echo'), 'echo', "assertEqual")
        self.assertNotEqual(self.thingy.echo('echo'), 'schplecho', "assertEqual")
        self.assertTrue(self.thingy.echo('echo') == 'echo', "assertTrue (object attribute)")
        self.assertFalse(self.thingy.echo('echo') != 'echo', 'assertFalse')

        with self.assertRaises(HoleyMoleyException):
            self.thingy.echo("quit")
            self.fail('should have raised HoleyMoleyException')


def pek_skip_decorator():
    return unittest.skip('')


class TestGrokUnitTest_skip_various_ways(unittest.TestCase):
    @unittest.skip('')
    def test_skip(self):
        self.fail('')

    # also: skipUnless
    @unittest.skipIf(sys.platform == 'linux', 'skip if on Linux')
    def test_skipIf(self):
        print('sanity')
        self.fail('')

    def test_skip_explicitly(self):
        self.skipTest('')
        self.fail('')

    def test_skip_explicitly_with_raise(self):
        raise unittest.SkipTest('')
        self.fail('')

    @pek_skip_decorator()
    def test_skip_decorator(self):
        self.fail('')


class TestGrokUnitTest_skips_from_setUp(unittest.TestCase):
    def setUp(self):
        self.skipTest('')

    def test_fails(self):
        self.fail('')


class TestGrokUnitTest_skips_from_setUp_via_raise(unittest.TestCase):
    def setUp(self):
        raise unittest.SkipTest('')
        self.fail('')

    def test_fails(self):
        self.fail('')


@unittest.skip('')
class TestGrokUnitTest_skip_class(unittest.TestCase):
    def test_skip(self):
        self.fail('')


class TestGrokUnitTest_expected(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertTrue(False, "intentional fail")


class TestGrokUnitTest_TestSuite(unittest.TestCase):
    def test_basic_functionality(self):
        runner = unittest.TextTestRunner()
        suite = unittest.TestSuite()
        suite.addTest(TestGrokUnitTest('test_basic_functionality'))
        runner.run(suite)


class TestGrokUnitTest_subTest(unittest.TestCase):
    def test_subTest(self):
        characters = ['Jyn', 'Galen']
        for character in characters:
            with self.subTest(label=character):
                self.assertTrue(character in characters, "subTest test")


def legacy_test():
    assert 2 + 2 == 5


# "Re-using old test code": needs a clearer example of this
class TestGrokUnitTests_legacy(unittest.TestCase):
    def test_basic_functionality(self):
        legacy_test_obj = unittest.FunctionTestCase(legacy_test)
        # unittest.result.TestResult
        test_result = legacy_test_obj.run()
        self.assertFalse(test_result.wasSuccessful(), "legacy test (clunky)")


class TestGrokUnitTests_trivia(unittest.TestCase):
    def test_assertRaises_alternate_syntax(self):
        thingy = PekObj()

        # alternate syntax for assertRaise
        # self.assertRaises(excClass, callable, *args)
        self.assertRaises(HoleyMoleyException, thingy.echo, "quit")
        self.assertRaises(HoleyMoleyException, echo, "quit")

        ## in case I don't remember the syntax (above is better...)
        try:
            thingy.echo('pek')
            self.fail("explicit failure (but won't get here")
        except(HoleyMoleyException, Exception):
            pass


class HoleyMoleyException(Exception):
    pass


class PekObj:
    def echo(self, arg):
        return echo(arg)


def echo(arg):
    if arg == "quit":
        raise HoleyMoleyException
    return arg

# NOTES
# less common syntax invocation
# python3 -m unittest test_grok_unittest.TestGrokUnitTest [-v]
# python3 -m unittest test_grok_unittest.TestGrokUnitTest.test_name [-v]

# note: does not find .py files with dashes!?
# not a valid identifier for a package or module
# https://docs.python.org/3/reference/lexical_analysis.html#identifiers

# TODO
# skip in relation to setUpClass, tearDownClass, setUpModule, tearDownModule
