from grokking_dp.longest_common_substring.longest_common_subsequence.main import find_lcs_length


def test_1():
    assert find_lcs_length("abdca", "cbda") == 3


def test_2():
    assert find_lcs_length("passport", "ppsspt") == 5
