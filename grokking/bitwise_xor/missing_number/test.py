from grokking.bitwise_xor.missing_number.main import find_missing_number


def test_1():
    assert find_missing_number([1, 5, 2, 6, 4]) == 3

def test_2():
    assert find_missing_number([1, 3, 4, 5, 6, 7, 2, 9, 10]) == 8
