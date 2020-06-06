from unittest import TestCase, main
from leet.length_of_longest_substring.main import Solution

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(3, s.lengthOfLongestSubstring('abcabcbb'))

    def test_2(self):
        self.assertEqual(1, s.lengthOfLongestSubstring('bbbbb'))

    def test_3(self):
        self.assertEqual(3, s.lengthOfLongestSubstring('pwwkew'))

    def test_4(self):
        self.assertEqual(0, s.lengthOfLongestSubstring(''))

    def test_5(self):
        self.assertEqual(3, s.lengthOfLongestSubstring('dvdf'))

    def test_5(self):
        self.assertEqual(5, s.lengthOfLongestSubstring('anviaj'))

if __name__ == '__main__':
    main()
