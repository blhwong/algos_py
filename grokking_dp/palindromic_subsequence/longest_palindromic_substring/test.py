from grokking_dp.palindromic_subsequence.longest_palindromic_substring.main import find_lps_length, find_lps_length_recursive, find_lps_length_iterative


def test_1():
    assert find_lps_length("abdbca") == 3


def test_2():
    assert find_lps_length("cddpd") == 3


def test_3():
    assert find_lps_length("pqr") == 1


def test_4():
    assert find_lps_length_recursive("abdbca") == 3


def test_5():
    assert find_lps_length_recursive("cddpd") == 3


def test_6():
    assert find_lps_length_recursive("pqr") == 1


def test_7():
    assert find_lps_length_iterative("abdbca") == 3


def test_8():
    assert find_lps_length_iterative("cddpd") == 3


def test_9():
    assert find_lps_length_iterative("pqr") == 1
