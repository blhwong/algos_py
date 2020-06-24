from unittest import TestCase, main
from algo_exp.three_largest_numbers.main import findThreeLargestNumbers


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(findThreeLargestNumbers([10, 5, 9, 10, 12]), [10, 10, 12])

    def test_2(self):
        self.assertListEqual(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])


if __name__ == '__main__':
    main()
