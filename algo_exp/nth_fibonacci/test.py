from algo_exp.nth_fibonacci.main import get_nth_fib


def test_1():
    assert get_nth_fib(1) == 0

def test_2():
    assert get_nth_fib(2) == 1

def test_3():
    assert get_nth_fib(3) == 1

def test_4():
    assert get_nth_fib(4) == 2

def test_5():
    assert get_nth_fib(5) == 3

def test_6():
    assert get_nth_fib(6) == 5

def test_7():
    assert get_nth_fib(7) == 8

def test_8():
    assert get_nth_fib(8) == 13
