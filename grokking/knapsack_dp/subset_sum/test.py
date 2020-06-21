from unittest import TestCase, main
from grokking.knapsack_dp.subset_sum.main import has_sum


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(has_sum([1, 2, 3, 7], 6))

    def test_2(self):
        self.assertTrue(has_sum([1, 2, 7, 1, 5], 10))

    def test_3(self):
        self.assertFalse(has_sum([1, 3, 4, 8], 6))


if __name__ == '__main__':
    main()
