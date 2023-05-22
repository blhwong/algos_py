from grokking_dp.palindromic_subsequence.min_deletions_to_palindrome.main import find_minimum_deletions


def test_1():
    assert find_minimum_deletions("abdbca") == 1


def test_2():
    assert find_minimum_deletions("cddpd") == 2


def test_3():
    assert find_minimum_deletions("pqr") == 2
