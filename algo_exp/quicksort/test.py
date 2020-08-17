from algo_exp.quicksort.main import quickSort


def test_1():
    array = [8, 5, 2, 9, 7, 6, 3]
    assert quickSort(array) == [2, 3, 5, 6, 7, 8, 9]

def test_2():
    array = [7, 20, 6, 17, 15, 12, 2, 19, 14, 3,
                1, 16, 18, 5, 8, 10, 21, 4, 11, 13, 9]
    assert quickSort(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
