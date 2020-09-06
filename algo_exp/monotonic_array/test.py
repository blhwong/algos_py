from algo_exp.monotonic_array.main import is_monotonic


def test_1():
    assert is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]) is True

def test_2():
    assert is_monotonic([1, 2, 3, 4, 5, 6, 7]) is True

def test_3():
    assert is_monotonic([1, 1, 1, 1, 1, 1, 1]) is True

def test_4():
    assert is_monotonic([1, 0, 1]) is False

def test_5():
    assert is_monotonic([0, 1, 2, 2, 1]) is False
