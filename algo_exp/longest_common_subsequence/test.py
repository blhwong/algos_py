from unittest import TestCase, main
from algo_exp.longest_common_subsequence.main import longestCommonSubsequence


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(longestCommonSubsequence('ZXVVYZW', 'XKYKZPW'), ['X', 'Y', 'Z', 'W'])

    def test_2(self):
        self.assertListEqual(longestCommonSubsequence('clement', 'antoine'), ['n', 't'])

    def test_3(self):
        self.assertListEqual(longestCommonSubsequence('abcba', 'abcbcba'), ['a', 'b', 'c', 'b', 'a'])

if __name__ == '__main__':
    main()
