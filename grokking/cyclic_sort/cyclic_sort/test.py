from grokking.cyclic_sort.cyclic_sort.main import cyclic_sort


def test_1():
    arr = [3, 1, 5, 4, 2]
    cyclic_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_2():
    arr = [2, 6, 4, 3, 1, 5]
    cyclic_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6]

def test_3():
    arr = [1, 5, 6, 4, 3, 2]
    cyclic_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6]
