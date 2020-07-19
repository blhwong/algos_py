from unittest import TestCase, main
from algo_exp.max_sum_increasing_subsequence.main import maxSumIncreasingSubsequence


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]), [110, [10, 20, 30, 50]])


    def test_2(self):
        self.assertListEqual(maxSumIncreasingSubsequence([-1]), [-1, [-1]])


    def test_3(self):
        self.assertListEqual(maxSumIncreasingSubsequence([-5, -4, -3, -2, -1]), [-1, [-1]])

    def test_4(self):
        self.assertListEqual(maxSumIncreasingSubsequence([-1, 1]), [1, [1]])

if __name__ == '__main__':
    main()
