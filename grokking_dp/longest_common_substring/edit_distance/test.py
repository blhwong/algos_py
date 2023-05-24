from grokking_dp.longest_common_substring.edit_distance.main import find_min_operations


def test_1():
    assert find_min_operations("bat", "but") == 1


def test_2():
    assert find_min_operations("abdca", "cbda") == 2


def test_3():
    assert find_min_operations("passpot", "ppsspqrt") == 3
