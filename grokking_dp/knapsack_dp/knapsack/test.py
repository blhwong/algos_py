from grokking_dp.knapsack_dp.knapsack.main import solve_knapsack_recursive, solve_knapsack_iterative


def test_1():
    weights = [1, 2, 3, 5]
    profits = [1, 6, 10, 16]
    assert solve_knapsack_recursive(profits, weights, 7) == 22

def test_2():
    weights = [1, 2, 3, 5]
    profits = [1, 6, 10, 16]
    assert solve_knapsack_iterative(profits, weights, 7) == 22

def test_3():
    weights = [1, 2, 3, 5]
    profits = [1, 6, 10, 16]
    assert solve_knapsack_iterative(profits, weights, 1) == 1

def test_4():
    weights = [2, 3, 1, 4]
    profits = [4, 5, 3, 7]
    assert solve_knapsack_recursive(profits, weights, 5) == 10

def test_5():
    weights = [2, 3, 1, 4]
    profits = [4, 5, 3, 7]
    assert solve_knapsack_iterative(profits, weights, 5) == 10
