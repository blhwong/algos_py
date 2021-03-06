from unittest import TestCase, main
from algo_exp.group_anagrams.main import group_anagrams


class TestSuite(TestCase):

    def test_1(self):
        expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertCountEqual(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']), expected)

    def test_2(self):
        expected = [['yo', 'oy',], ['flop', 'olfp'], ['act', 'tac', 'cat']]
        self.assertCountEqual(group_anagrams(['yo', 'act', 'flop', 'tac', 'cat', 'oy', 'olfp']), expected)


if __name__ == '__main__':
    main()
