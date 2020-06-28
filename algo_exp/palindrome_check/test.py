from unittest import TestCase, main
from algo_exp.palindrome_check.main import isPalindrome


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(isPalindrome('abcdcba'))

    def test_2(self):
        self.assertFalse(isPalindrome('abcde'))


if __name__ == '__main__':
    main()
