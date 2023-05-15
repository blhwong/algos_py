from grokking_dp.knapsack_dp.minimum_subset_sum_difference.main import get_minimum_subset_difference_iterative, get_minimum_subset_difference_recursive


def test_1():
    assert get_minimum_subset_difference_iterative([1, 2, 3, 9]) == 3

def test_2():
    assert get_minimum_subset_difference_iterative([1, 2, 7, 1, 5]) == 0

def test_3():
    assert get_minimum_subset_difference_iterative([1, 3, 100, 4]) == 92

def test_4():
    assert get_minimum_subset_difference_recursive([1, 2, 3, 9]) == 3

def test_5():
    assert get_minimum_subset_difference_recursive([1, 2, 7, 1, 5]) == 0

def test_6():
    assert get_minimum_subset_difference_recursive([1, 3, 100, 4]) == 92

def test_7():
    assert get_minimum_subset_difference_iterative([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0

def test_8():
    assert get_minimum_subset_difference_recursive([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
