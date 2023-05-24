from grokking_dp.longest_common_substring.shortest_common_supersequence.main import find_scs_length_recursive, find_scs_length_iterative


def test_1():
    assert find_scs_length_recursive("abcf", "bdcf") == 5


def test_2():
    assert find_scs_length_recursive("dynamic", "programming") == 15


def test_3():
    assert find_scs_length_recursive("abc", "def") == 6


def test_4():
    assert find_scs_length_iterative("abcf", "bdcf") == 5


def test_5():
    assert find_scs_length_iterative("dynamic", "programming") == 15


def test_6():
    assert find_scs_length_iterative("abc", "def") == 6
