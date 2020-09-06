from algo_exp.nth_fibonacci.main import get_nth_fib


def test_1():
    assert get_nth_fib(2) == 1

def test_2():
    assert get_nth_fib(6) == 5
