import unittest
import re


class GrokRe(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertFalse(re.match('Hello', 'hello'))
        self.assertTrue(re.match('Hello', 'hello', re.I))

        # note: I contend that seeing re.match examples w/^ and $ are silly
        # howto-regex: use 'search' if your 'match' starts w/.*;
        #   seems that ^ and $ would also fit that
        self.assertTrue(re.match('^hello$', 'hello'))
        self.assertFalse(re.match('world', 'hello world'))
        self.assertTrue(re.search('world', 'hello world'))

        phrase = 'This is a test of the emergency broadcast system'
        self.assertEqual(len(re.split('\s', phrase)), 9)  # noqa: W605
        split = (re.split('\s', phrase, maxsplit=4))  # noqa: W605
        self.assertEqual(len(split), 5)
        self.assertEqual(split[:4], ['This', 'is', 'a', 'test'])

        # 're.sub' returns a string
        cindy = re.sub('s', 'th', phrase)
        self.assertEqual(
            cindy, 'Thith ith a tetht of the emergency broadcatht thythtem')

        # non-overlapping
        self.assertEqual(len(re.findall('baba', 'babababa')), 2)

        # p 205: mnenomic: pobj is a RE *P*attern object (sheesh...)
        _re = '((?P<yr>\d{4})-(?P<mon>\d{2})-(?P<date>\d{2}))'  # noqa: W605
        pobj = re.compile(_re)
        self.assertFalse(pobj.match('Happy unbirthday!'))

        date = '2020-07-22'
        mobj_date = pobj.match('2020-07-22')
        self.assertTrue(mobj_date)
        self.assertEqual(mobj_date.groupdict(), {
                         'yr': '2020', 'mon': '07', 'date': '22'})
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
