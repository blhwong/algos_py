from grokking.cyclic_sort.find_missing_number.main import find_missing_number


def test_1():
    assert find_missing_number([4, 0, 3, 1]) == 2


def test_2():
    assert find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]) == 7

def test_3():
    assert find_missing_number([4, 2, 0, 1, 3]) == 5
