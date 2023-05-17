from grokking_dp.unbounded_knapsack.minimum_coin_change.main import count_change


def test_1():
    assert count_change([1, 2, 3], 5) == 2

def test_2():
    assert count_change([1, 2, 3], 7) == 3
