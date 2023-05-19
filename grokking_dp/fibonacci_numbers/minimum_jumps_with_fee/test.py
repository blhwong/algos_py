from grokking_dp.fibonacci_numbers.minimum_jumps_with_fee.main import find_min_fee_recursive, find_min_fee_iterative


def test_1():
    assert find_min_fee_recursive([1, 2, 5, 2, 1, 2]) == 3


def test_2():
    assert find_min_fee_recursive([2, 3, 4, 5]) == 5


def test_3():
    assert find_min_fee_iterative([1, 2, 5, 2, 1, 2]) == 3


def test_4():
    assert find_min_fee_iterative([2, 3, 4, 5]) == 5
