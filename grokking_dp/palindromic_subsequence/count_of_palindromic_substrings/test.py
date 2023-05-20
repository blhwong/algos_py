from grokking_dp.palindromic_subsequence.count_of_palindromic_substrings.main import count_palindromic_substrings, count_palindromic_substrings_recursive, count_palindromic_substrings_iterative


def test_1():
    assert count_palindromic_substrings("abdbca") == 7


def test_2():
    assert count_palindromic_substrings("cddpd") == 7


def test_3():
    assert count_palindromic_substrings("pqr") == 3


def test_4():
    assert count_palindromic_substrings_recursive("abdbca") == 7


def test_5():
    assert count_palindromic_substrings_recursive("cddpd") == 7


def test_6():
    assert count_palindromic_substrings_recursive("pqr") == 3


def test_7():
    assert count_palindromic_substrings_iterative("abdbca") == 7


def test_8():
    assert count_palindromic_substrings_iterative("cddpd") == 7


def test_9():
    assert count_palindromic_substrings_iterative("pqr") == 3
