## python3 -m unittest [-v]
## note: does not find .py files with dashes!?
## not a valid identifier for a package or module
## https://docs.python.org/3/reference/lexical_analysis.html#identifiers

## python3 -m unittest test_grok_unittest[.py] [-v]
## python3 -m unittest test_grok_unittest.TestGrokUnitTest [-v]
## python3 -m unittest test_grok_unittest.TestGrokUnitTest.test_basic_functionality [-v]

import unittest

class HoleyMoleyException(Exception):
    pass

class PekObj:
    def echo(self, arg):
        return echo(arg)

def echo(arg):
    if arg == "quit":
        raise HoleyMoleyException
    return arg

## assertEqual, assertNotEqual, assertTrue, assertFalse
## assertRaises, fail
class TestGrokUnitTest(unittest.TestCase):
    def setUp(self):
        self.thingy = PekObj()

    def tearDown(self):
        pass
                
    def test_basic_functionality(self):
        self.assertEqual(self.thingy.echo('echo'), 'echo', "assertEqual")
        self.assertTrue(self.thingy.echo('echo') == 'echo', "assertTrue (object attribute)")
        self.assertFalse(self.thingy.echo('echo') != 'echo', 'assertFalse')

        with self.assertRaises(HoleyMoleyException):
            self.thingy.echo("quit")
            self.fail('should have raised HoleyMoleyException')

    def test_assertRaises_alternate_syntax(self):
        ## alternate syntax for assertRaise
        ## self.assertRaises(excClass, callable, *args)
        self.assertRaises(HoleyMoleyException, self.thingy.echo, "quit")
        self.assertRaises(HoleyMoleyException, echo, "quit")

        ## in case I don't remember the syntax (above is better...)
        try:
            self.thingy.echo('pek')
            self.fail("explicit failure (but won't get here")
        except(HoleyMoleyException, Exception) as e:
            pass

            
