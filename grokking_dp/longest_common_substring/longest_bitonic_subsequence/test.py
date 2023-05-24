from grokking_dp.longest_common_substring.longest_bitonic_subsequence.main import find_lbs_length


def test_1():
    assert find_lbs_length([4, 2, 3, 6, 10, 1, 12]) == 5


def test_2():
    assert find_lbs_length([4, 2, 5, 9, 7, 6, 10, 3, 1]) == 7
