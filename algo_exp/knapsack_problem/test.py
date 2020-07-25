from unittest import TestCase, main
from algo_exp.knapsack_problem.main import knapsackProblem


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10), [10, [1, 3]])


if __name__ == '__main__':
    main()
