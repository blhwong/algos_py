from unittest import TestCase, main
from leet.group_anagrams.main import Solution

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertCountEqual(s.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']), expected)


if __name__ == '__main__':
    main()
