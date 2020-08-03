import unittest
import sys
import string

# note: page numbers refer to 'Python Pocket Reference, 5th edition'


class GrokStrings(unittest.TestCase):
    # 'Table 3' on p 17-18
    def test_sequence_operations(self):
        self.assertTrue('a' in 'this is a test')
        self.assertTrue('test' in 'this is a test')
        self.assertTrue('winston!' not in 'this is a test')
        self.assertEqual('win' + 'ston!', 'winston!')
        self.assertEqual('winnie' * 2, 'winniewinnie')
        # I disapprove of this string syntax feature...
        self.assertEqual('winnie' * 2, 'winnie' 'winnie')
        self.assertEqual('winston!'[-1], '!')
        self.assertEqual('winston!'[:5], 'winst')
        self.assertEqual(len('winston!'), 8)
        self.assertEqual(min('winston!'), '!')

        _iter = iter('winston!')
        self.assertEqual(next(_iter), 'w')

        pek = []
        for x in 'winston!':
            pek.append(x)
        self.assertEqual(''.join(pek), 'winston!')

        pek = []
        [pek.append(x) for x in 'winston!']
        self.assertEqual(''.join(pek), 'winston!')

        def func(x):
            self.assertEqual(len(x), 1)
            return x
        pek = list(map(func, 'winston!'))
        self.assertEqual(''.join(pek), 'winston!')

    # p 28-30
    def test_string_formating_expression(self):
        self.assertEqual('%s %s %.2f' % (42, 'spam', 1/3.0), '42 spam 0.33')
        # string format method
        self.assertEqual('{0} {1} {2:.2f}'.format(
            42, 'spam', 1/3.0), '42 spam 0.33')
        # f-string
        pek = ['42', 'spam', 1/3.0]
        self.assertEqual(f'{pek[0]} {pek[1]} {pek[2]:.2f}', '42 spam 0.33')

        # more string format expression
        self.assertEqual('%+.*f' % (4, -1/3.0), '-0.3333')
        self.assertEqual('%(x)s' % dict(x='winston!'), 'winston!')
        self.assertEqual('%(x)04d' % dict(x=21), '0021')

    # p 30-33
    def test_string_formating_method(self):
        self.assertEqual('{} {} {:.2f}'.format(
            42, 'spam', 1/3.0), '42 spam 0.33')
        self.assertEqual('{d} {s}'.format(d=42, s='spam'), '42 spam')
        # w/dict unpacking
        self.assertEqual('{d} {s}'.format(
            **dict(d=42, s='spam')), '42 spam')
        # pg 30: the '<6s' is align (p 33)
        self.assertEqual('[{:<6s}]'.format('spam'), '[spam  ]')

        self.assertEqual('{0.platform} {1[x]} {2[0]}'.format(
            sys, dict(x='spam'), [42]), 'linux spam 42')

        # w/commas!
        self.assertEqual('{0:,d}'.format(2**32), '4,294,967,296')
        # * fill, ^ center align, + sign
        self.assertEqual('|{0:*^+16d}|'.format(2**16), '|*****+65536*****|')
        # width and precision
        self.assertEqual('|{:12.2f}|'.format(2**16/3), '|    21845.33|')

    # p 34
    def test_string_template_string_substitution(self):
        self.assertEqual('%(page)i: %(book)s' %
                         {'page': 2, 'book': 'PR5E'}, '2: PR5E')
        self.assertEqual('%(page)i: %(book)s' %
                         dict(page=2, book='PR5E'), '2: PR5E')

    # p 34
    def test_string_Template_class(self):
        template = string.Template('$page: $book')
        self.assertEqual(template.substitute(
            {'page': 2, 'book': 'PR5E'}), '2: PR5E')
        # Template class substitution w/keyword arguments
        self.assertEqual(template.substitute(page=2, book='PR5E'), '2: PR5E')
        self.assertEqual(template.substitute(
            dict(page=2, book='PR5E')), '2: PR5E')
        self.assertEqual(template.substitute(
            {'page': 2, 'book': 'PR5E'}), '2: PR5E')
