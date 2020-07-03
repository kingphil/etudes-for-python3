## python3 -m unittest [-v]
## python3 -m unittest test_grok_unittest[.py] [-v]
## python3 -m unittest -k <pattern>
## python3 -m unittest discover -s <directory>

import unittest

## assertEqual, assertNotEqual, assertTrue, assertFalse
## assertRaises, fail
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

class TestGrokUnitTest_TestSuite(unittest.TestCase):
    def test_basic_functionality(self):
        runner = unittest.TextTestRunner()
        suite = unittest.TestSuite()
        suite.addTest(TestGrokUnitTest('test_basic_functionality'))
        runner.run(suite)

class TestGrokUnitTests_trivia(unittest.TestCase):
    def test_assertRaises_alternate_syntax(self):
        thingy = PekObj()

        ## alternate syntax for assertRaise
        ## self.assertRaises(excClass, callable, *args)
        self.assertRaises(HoleyMoleyException, thingy.echo, "quit")
        self.assertRaises(HoleyMoleyException, echo, "quit")

        ## in case I don't remember the syntax (above is better...)
        try:
            thingy.echo('pek')
            self.fail("explicit failure (but won't get here")
        except(HoleyMoleyException, Exception) as e:
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

### NOTES
## less common syntax invocation
## python3 -m unittest test_grok_unittest.TestGrokUnitTest [-v]
## python3 -m unittest test_grok_unittest.TestGrokUnitTest.test_basic_functionality [-v]

## note: does not find .py files with dashes!?
## not a valid identifier for a package or module
## https://docs.python.org/3/reference/lexical_analysis.html#identifiers
