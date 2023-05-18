from grokking_dp.fibonacci_numbers.staircase.main import count_ways_iterative, count_ways_recursive


def test_1():
    assert count_ways_iterative(3) == 4


def test_2():
    assert count_ways_iterative(4) == 7


def test_3():
    assert count_ways_iterative(5) == 13


def test_4():
    assert count_ways_recursive(3) == 4


def test_5():
    assert count_ways_recursive(4) == 7


def test_6():
    assert count_ways_recursive(5) == 13


def test_7():
    assert count_ways_iterative(1) == 1


def test_8():
    assert count_ways_recursive(1) == 1
