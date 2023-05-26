from grokking_dp.longest_common_substring.max_sum_increasing_subsequence.main import find_msis_recursive, find_msis_iterative


def test_1():
    assert find_msis_recursive([4, 1, 2, 6, 10, 1, 12]) == 32


def test_2():
    assert find_msis_recursive([-4, 10, 3, 7, 15]) == 25


def test_3():
    assert find_msis_iterative([4, 1, 2, 6, 10, 1, 12]) == 32


def test_4():
    assert find_msis_iterative([-4, 10, 3, 7, 15]) == 25


def test_5():
    assert find_msis_recursive([4, 2, 5, 9, 7, 6, 10, 3, 1]) == 28


def test_6():
    assert find_msis_iterative([4, 2, 5, 9, 7, 6, 10, 3, 1]) == 28
