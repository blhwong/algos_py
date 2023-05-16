from grokking_dp.knapsack_dp.find_target_subsets.main import find_target_subsets_recursive, find_target_subsets_iterative


def test_1():
    assert find_target_subsets_recursive([1, 1, 2, 3], 1) == 3


def test_2():
    assert find_target_subsets_recursive([1, 2, 7, 1], 9) == 2

def test_3():
    assert find_target_subsets_iterative([1, 1, 2, 3], 1) == 3

def test_4():
    assert find_target_subsets_iterative([1, 2, 7, 1], 9) == 2
