from unittest import TestCase, main
from algo_exp.longest_palindromic_substring.main import longestPalindromicSubstring


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(longestPalindromicSubstring('abaxyzzyxf'), 'xyzzyx')

    def test_2(self):
        self.assertEqual(longestPalindromicSubstring('a'), 'a')

    def test_3(self):
        self.assertEqual(longestPalindromicSubstring(''), '')

if __name__ == '__main__':
    main()
