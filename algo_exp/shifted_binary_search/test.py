from algo_exp.shifted_binary_search.main import shifted_binary_search


def test_1():
    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    assert shifted_binary_search(array, 33) == 8


def test_2():
    array = [5, 23, 111, 1]
    assert shifted_binary_search(array, 111) == 2


def test_3():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert shifted_binary_search(array, 7) == 6
