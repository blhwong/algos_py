from grokking_dp.fibonacci_numbers.fibonacci_numbers.main import calculate_fibonacci


def test_1():
    assert calculate_fibonacci(5) == 5


def test_2():
    assert calculate_fibonacci(6) == 8


def test_3():
    assert calculate_fibonacci(7) == 13


def test_4():
    assert calculate_fibonacci(0) == 0
