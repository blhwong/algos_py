from unittest import TestCase, main
from algo_exp.validate_subsequence.main import isValidSubsequence


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))

    def test_2(self):
        self.assertFalse(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 12]))

    def test_3(self):
        self.assertTrue(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]))

if __name__ == '__main__':
    main()
