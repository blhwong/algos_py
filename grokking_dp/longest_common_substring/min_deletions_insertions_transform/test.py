from grokking_dp.longest_common_substring.min_deletions_insertions_transform. main import find_mdi


def test_1():
    assert find_mdi("abc", "fbc") == (1, 1)


def test_2():
    assert find_mdi("abdca", "cbda") == (2, 1)


def test_3():
    assert find_mdi("passport", "ppsspt") == (3, 1)
