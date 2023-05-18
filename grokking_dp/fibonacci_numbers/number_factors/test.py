from grokking_dp.fibonacci_numbers.number_factors.main import count_ways_recursive, count_ways_iterative


def test_1():
    assert count_ways_recursive(4) == 4


def test_2():
    assert count_ways_recursive(5) == 6


def test_3():
    assert count_ways_recursive(6) == 9


def test_4():
    assert count_ways_iterative(4) == 4


def test_5():
    assert count_ways_iterative(5) == 6


def test_6():
    assert count_ways_iterative(6) == 9


def test_7():
    assert count_ways_recursive(2) == 1


def test_8():
    assert count_ways_iterative(2) == 1
