from grokking_dp.longest_common_substring.longest_common_substring.main import find_lcs_length


def test_1():
    assert find_lcs_length("abdca", "cbda") == 2


def test_2():
    assert find_lcs_length("passport", "ppsspt") == 3
