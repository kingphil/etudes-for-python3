import unittest

# note: page numbers refer to 'Python Pocket Reference, 5th edition'


class GrokStrings(unittest.TestCase):
    # "Table 3" on p 17-18
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
            return x
        pek = list(map(func, 'winston!'))
        self.assertEqual(''.join(pek), 'winston!')
