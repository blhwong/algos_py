from unittest import TestCase, main
from grokking.knapsack_dp.knapsack.main import solve_knapsack_recursive, solve_knapsack_iterative


class TestSuite(TestCase):
    def test_1(self):
        weights = [1, 2, 3, 5]
        profits = [1, 6, 10, 16]
        self.assertEqual(solve_knapsack_recursive(profits, weights, 7), 22)


    def test_2(self):
        weights = [1, 2, 3, 5]
        profits = [1, 6, 10, 16]
        self.assertEqual(solve_knapsack_iterative(profits, weights, 7), 22)

    def test_3(self):
        weights = [1, 2, 3, 5]
        profits = [1, 6, 10, 16]
        self.assertEqual(solve_knapsack_iterative(profits, weights, 1), 1)

if __name__ == '__main__':
    main()
