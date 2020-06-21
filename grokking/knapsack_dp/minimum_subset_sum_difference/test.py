from unittest import TestCase, main
from grokking.knapsack_dp.minimum_subset_sum_difference.main import get_minimum_subset_difference_iterative, get_minimum_subset_difference_recursive


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(get_minimum_subset_difference_iterative([1, 2, 3, 9]), 3)

    def test_2(self):
        self.assertEqual(get_minimum_subset_difference_iterative([1, 2, 7, 1, 5]), 0)

    def test_3(self):
        self.assertEqual(get_minimum_subset_difference_iterative([1, 3, 100, 4]), 92)

    def test_4(self):
        self.assertEqual(get_minimum_subset_difference_recursive([1, 2, 3, 9]), 3)

    def test_5(self):
        self.assertEqual(get_minimum_subset_difference_recursive([1, 2, 7, 1, 5]), 0)

    def test_6(self):
        self.assertEqual(get_minimum_subset_difference_recursive([1, 3, 100, 4]), 92)

    def test_7(self):
        self.assertEqual(get_minimum_subset_difference_iterative([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 0)

    def test_8(self):
        self.assertEqual(get_minimum_subset_difference_recursive([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 0)

if __name__ == '__main__':
    main()
