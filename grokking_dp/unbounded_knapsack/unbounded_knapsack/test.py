from grokking_dp.unbounded_knapsack.unbounded_knapsack.main import solve_knapsack_recursive, solve_knapsack_iterative


def test_1():
    assert solve_knapsack_recursive([15, 50, 60, 90], [1, 3, 4, 5], 8) == 140


def test_2():
    assert solve_knapsack_recursive([15, 50, 60, 90], [1, 3, 4, 5], 6) == 105


def test_3():
    assert solve_knapsack_recursive([15, 20, 50], [1, 2, 3], 5) == 80


def test_4():
    assert solve_knapsack_iterative([15, 50, 60, 90], [1, 3, 4, 5], 8) == 140


def test_5():
    assert solve_knapsack_iterative([15, 50, 60, 90], [1, 3, 4, 5], 6) == 105


def test_6():
    assert solve_knapsack_iterative([15, 20, 50], [1, 2, 3], 5) == 80
