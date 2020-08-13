from unittest import TestCase, main
from algo_exp.palindrome_partitioning_min_cuts.main import palindromePartitioningMinCuts


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(palindromePartitioningMinCuts('noonabbad'), 2)

    # def test_2(self):
    #     self.assertEqual(palindromePartitioningMinCuts('a'), 0)

    # def test_3(self):
    #     self.assertEqual(palindromePartitioningMinCuts('abbba'), 0)

    # def test_4(self):
    #     self.assertEqual(palindromePartitioningMinCuts('ababbbabbababa'), 3)


if __name__ == '__main__':
    main()
