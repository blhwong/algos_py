from grokking_dp.longest_common_substring.longest_alternating_subsequence.main import find_las_length


def test_1():
    assert find_las_length([1, 2, 3, 4]) == 2


def test_2():
    assert find_las_length([3, 2, 1, 4]) == 3


def test_3():
    assert find_las_length([1, 3, 2, 4]) == 4
