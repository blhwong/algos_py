from grokking.two_pointers.dutch_flag_sort.main import dutch_flag_sort


def test_1():
    arr = [1, 0, 2, 1, 0]
    expected = [0, 0, 1, 1, 2]
    dutch_flag_sort(arr)
    assert arr == expected

def test_2():
    arr = [2, 2, 0, 1, 2, 0]
    expected = [0, 0, 1, 2, 2, 2]
    dutch_flag_sort(arr)
    assert arr == expected
