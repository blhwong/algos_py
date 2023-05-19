from grokking_dp.fibonacci_numbers.house_thief.main import find_max_steal_iterative, find_max_steal_recursive


def test_1():
    assert find_max_steal_iterative([2, 5, 1, 3, 6, 2, 4]) == 15


def test_2():
    assert find_max_steal_iterative([2, 10, 14, 8, 1]) == 18


def test_3():
    assert find_max_steal_iterative([2]) == 2


def test_4():
    assert find_max_steal_iterative([2, 5]) == 5


def test_5():
    assert find_max_steal_recursive([2, 5, 1, 3, 6, 2, 4]) == 15


def test_6():
    assert find_max_steal_recursive([2, 10, 14, 8, 1]) == 18


def test_7():
    assert find_max_steal_recursive([2]) == 2


def test_8():
    assert find_max_steal_recursive([2, 5]) == 5
