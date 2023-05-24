from grokking_dp.longest_common_substring.longest_repeating_subsequence.main import find_lrs_length


def test_1():
    assert find_lrs_length("tomorrow") == 2


def test_2():
    assert find_lrs_length("aabdbcec") == 3


def test_3():
    assert find_lrs_length("fmff") == 2
