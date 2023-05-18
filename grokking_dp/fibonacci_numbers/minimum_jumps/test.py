from grokking_dp.fibonacci_numbers.minimum_jumps.main import count_min_jumps_recursive, count_min_jumps_iterative


def test_1():
    assert count_min_jumps_recursive([2, 1, 1, 1, 4]) == 3


def test_2():
    assert count_min_jumps_recursive([1, 1, 3, 6, 9, 3, 0, 1, 3]) == 4


def test_3():
    assert count_min_jumps_iterative([2, 1, 1, 1, 4]) == 3


def test_4():
    assert count_min_jumps_iterative([1, 1, 3, 6, 9, 3, 0, 1, 3]) == 4
