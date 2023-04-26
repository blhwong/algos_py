from grokking.fast_slow_pointers.happy_number.main import find_happy_number


def test_1():
    assert find_happy_number(23)

def test_2():
    assert not find_happy_number(12)

