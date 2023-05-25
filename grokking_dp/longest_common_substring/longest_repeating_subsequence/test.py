from grokking_dp.longest_common_substring.longest_repeating_subsequence.main import find_lrs_length_recursive, find_lrs_length_iterative


def test_1():
    assert find_lrs_length_recursive("tomorrow") == 2


def test_2():
    assert find_lrs_length_recursive("aabdbcec") == 3


def test_3():
    assert find_lrs_length_recursive("fmff") == 2


def test_4():
    assert find_lrs_length_iterative("tomorrow") == 2


def test_5():
    assert find_lrs_length_iterative("aabdbcec") == 3


def test_6():
    assert find_lrs_length_iterative("fmff") == 2
