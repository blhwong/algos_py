from algo_exp.subarray_sort.main import subarraySort


def test_1():
    assert subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]) == [3, 9]

def test_2():
    assert subarraySort([1, 2, 3, 4, 5]) == [-1, -1]

def test_3():
    assert subarraySort([2, 1]) == [0, 1]

def test_4():
    assert subarraySort([
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        2,
    ]) == [2, 19]

def test_5():
    assert subarraySort([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == [-1, -1]
