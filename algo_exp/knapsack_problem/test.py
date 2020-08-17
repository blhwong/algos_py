from algo_exp.knapsack_problem.main import knapsackProblem


def test_1():
    assert knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10) == [10, [1, 3]]
