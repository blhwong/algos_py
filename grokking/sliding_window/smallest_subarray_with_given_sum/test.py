from grokking.sliding_window.smallest_subarray_with_given_sum.main import smallest_subarray_with_given_sum


def test_1():
    assert smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]) == 2

def test_2():
    assert smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]) == 1


def test_3():
    assert smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]) == 3

def test_4():
    assert smallest_subarray_with_given_sum(100, [3, 4, 1, 1, 6]) == 0
