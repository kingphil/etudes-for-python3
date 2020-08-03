import unittest

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
