from grokking_dp.unbounded_knapsack.rod_cutting.main import solve_rod_cutting


def test_1():
    assert solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5) == 14
