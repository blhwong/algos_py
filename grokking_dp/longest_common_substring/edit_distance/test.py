from grokking_dp.longest_common_substring.edit_distance.main import find_min_operations_iterative, find_min_operations_recursive


def test_1():
    assert find_min_operations_iterative("bat", "but") == 1


def test_2():
    assert find_min_operations_iterative("abdca", "cbda") == 2


def test_3():
    assert find_min_operations_iterative("passpot", "ppsspqrt") == 3


def test_4():
    assert find_min_operations_recursive("bat", "but") == 1


def test_5():
    assert find_min_operations_recursive("abdca", "cbda") == 2


def test_6():
    assert find_min_operations_recursive("passpot", "ppsspqrt") == 3
