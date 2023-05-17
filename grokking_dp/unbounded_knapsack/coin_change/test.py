from grokking_dp.unbounded_knapsack.coin_change.main import count_change


def test_1():
    assert count_change([1, 2, 3], 5) == 5
