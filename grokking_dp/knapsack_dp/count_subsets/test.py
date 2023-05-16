from grokking_dp.knapsack_dp.count_subsets.main import count_subsets


def test_1():
    assert count_subsets([1, 1, 2, 3], 4) == 3


def test_2():
    assert count_subsets([1, 2, 7, 1, 5], 9) == 3
