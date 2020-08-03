import unittest


class GrokExceptions(unittest.TestCase):
    # pg 163
    def test_specific_exceptions(self):
        for superclass in [BaseException, Exception, ArithmeticError,
                           ZeroDivisionError]:
            with self.assertRaises(superclass):
                70/0

        # todo: GeneratorExit: when is a generator's close() method called?
        # todo: StopIteration: similar to above
        # skip: FloatingPointError; good example is lacking in cpython test
        #   suite, as well
        # skip (impractical here): EOFError (depends on 'input'),
        #   KeyboardInterrupt, MemoryError, OverflowError,
        #   ReferenceError, SystemError, TabError, UnboundLocalError, Unicode*
        _mylist = "this is a test".split()
        with self.assertRaises(AssertionError):
            self.fail('')
        with self.assertRaises(AttributeError):
            print(self.does_not_exist)
        with self.assertRaises(ImportError):
            import non.existent.module
        with self.assertRaises(IndentationError):
            bad_code = '69\n\t70'
            eval(bad_code)
        with self.assertRaises(IndexError):
            _mylist[4] = "explosion"
        with self.assertRaises(KeyError):
            mymap = dict(enumerate(_mylist))
            print(mymap[4])
        with self.assertRaises(NameError):
            print(doesntExist)
        with self.assertRaises(RuntimeError):
            # see exception_hierarchy.txt in cpython
            raise NotImplementedError
        with self.assertRaises(SyntaxError):
            bad_code = 'while True pass'
            eval(bad_code)
        with self.assertRaises(SystemExit):
            # bonus factoid re: 'SystemExit' in 'Exception' on p 162;
            #   one of the few that does not inherit from Exception
            try:
                import sys
                sys.exit(0)
            except Exception:
                self.fail('')
        with self.assertRaises(ValueError):
            import os
            os.popen("ls -l /", mode="z")
