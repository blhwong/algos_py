from unittest import TestCase, main
from leet.longest_repeating_character_replacement.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.characterReplacement('ABAB', 2), 4)

    def test_2(self):
        self.assertEqual(s.characterReplacement('AABABBA', 1), 4)

    def test_3(self):
        self.assertEqual(s.characterReplacement('AACDEFEFEGHIJK', 2), 5)

    def test_4(self):
        self.assertEqual(s.characterReplacement('AAAA', 0), 4)

if __name__ == '__main__':
    main()
