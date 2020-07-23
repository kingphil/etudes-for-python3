import unittest
import re
from pprint import pprint as pp

class GrokRe(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertFalse(re.match('Hello', 'hello'))
        self.assertTrue(re.match('Hello', 'hello', re.I))

        # note: I contend that seeing re.match examples w/^ and $ are super duper silly
        # note: I still do not have clarity on if re.match or re.search is preferred
        self.assertTrue(re.match('^hello$', 'hello'))
        self.assertFalse(re.match('world', 'hello world'))
        self.assertTrue(re.search('world', 'hello world'))

        phrase = 'This is a test of the emergency broadcast system'
        self.assertEqual(len(re.split(' ', phrase)), 9)
        split = (re.split(' ', phrase, maxsplit=4))
        self.assertEqual(len(split), 5)
        self.assertEqual(split[:4], ['This', 'is', 'a', 'test'])

        # 're.sub' returns a string
        cindy = re.sub('s', 'th', phrase)
        self.assertEqual(cindy, 'Thith ith a tetht of the emergency broadcatht thythtem')

        # non-overlapping
        self.assertEqual(len(re.findall('baba', 'babababa')), 2)

        # p 205: mnenomic: pobj is a RE *P*attern object (sheesh...)
        pobj = re.compile('((?P<year>\d{4})-(?P<month>\d{2})-(?P<date>\d{2}))')
        self.assertFalse(pobj.match('Happy unbirthday!'))

        date = '2020-07-22'
        mobj_date = pobj.match('2020-07-22')
        self.assertTrue(mobj_date)
        self.assertEqual(mobj_date.groupdict(), {'year':'2020', 'month':'07', 'date':'22'})
        self.assertEqual(mobj_date.groups(), (date, '2020', '07', '22'))

        pobj_lookahead = re.compile('(?P<name>Isaac (?=Asimov))')
        mobj_lookahead = pobj_lookahead.match('Isaac Asimov')
        self.assertTrue(mobj_lookahead)
        # shows that assertion does not consume any of the string
        self.assertEqual(mobj_lookahead.groupdict()['name'], 'Isaac ')
        self.assertFalse(pobj_lookahead.match('Isaac Smith'))

        pobj_neg_lookahead = re.compile('(?P<name>Isaac (?!Asimov))')
        mobj_neg_lookahead = pobj_neg_lookahead.match('Isaac Smith')
        self.assertTrue(mobj_neg_lookahead)
        # shows that assertion does not consume any of the string
        self.assertEqual(mobj_neg_lookahead.groupdict()['name'], 'Isaac ')
        self.assertFalse(pobj_neg_lookahead.match('Isaac Asimov'))
