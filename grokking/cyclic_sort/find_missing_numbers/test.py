from grokking.cyclic_sort.find_missing_numbers.main import find_missing_numbers


def test_1():
    assert find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]) == [4, 6, 7]

def test_2():
    assert find_missing_numbers([2, 4, 1, 2]) == [3]

def test_3():
    assert find_missing_numbers([2, 3, 2, 1]) == [4]
