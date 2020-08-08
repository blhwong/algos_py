from unittest import TestCase, main
from algo_exp.longest_substring_without_duplication.main import longestSubstringWithoutDuplication


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(longestSubstringWithoutDuplication('clementisacap'), 'mentisac')

    def test_2(self):
        self.assertEqual(longestSubstringWithoutDuplication('abcb'), 'abc')

if __name__ == '__main__':
    main()
