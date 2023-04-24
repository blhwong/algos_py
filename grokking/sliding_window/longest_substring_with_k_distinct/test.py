from grokking.sliding_window.longest_substring_with_k_distinct.main import longest_substring_with_k_distinct


def test_1():
    assert longest_substring_with_k_distinct('araaci', 2) == 4


def test_2():
    assert longest_substring_with_k_distinct('araaci', 1) == 2


def test_3():
    assert longest_substring_with_k_distinct('araaci', 3) == 5
