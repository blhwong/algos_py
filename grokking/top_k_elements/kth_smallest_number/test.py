from grokking.top_k_elements.kth_smallest_number.main import find_Kth_smallest_number


def test_1():
    assert find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3) == 5

def test_2():
    assert find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4) == 5

def test_3():
    assert find_Kth_smallest_number([5, 12, 11, -1, 12], 3) == 11
