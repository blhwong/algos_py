from grokking.k_way_merge.smallest_number_range.main import find_smallest_range


def test_1():
    assert find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]]) == [4, 7]

def test_2():
    assert find_smallest_range([[1, 9], [4, 12], [7, 10, 16]]) == [9, 12]
