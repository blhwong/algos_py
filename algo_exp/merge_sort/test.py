from algo_exp.merge_sort.main import mergeSort


def test_1():
    assert mergeSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
