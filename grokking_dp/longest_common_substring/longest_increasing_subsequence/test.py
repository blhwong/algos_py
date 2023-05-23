from grokking_dp.longest_common_substring.longest_increasing_subsequence.main import find_lis_length, find_lis_length_recursive


def test_1():
    assert find_lis_length([4, 2, 3, 6, 10, 1, 12]) == 5


def test_2():
    assert find_lis_length([-4, 10, 3, 7, 15]) == 4


def test_3():
    assert find_lis_length([2, 3, 1, 2, 3, 4, 5]) == 5


def test_4():
    assert find_lis_length([2, 3, 1, 2, 3, 2, 3]) == 3


def test_5():
    assert find_lis_length_recursive([4, 2, 3, 6, 10, 1, 12]) == 5


def test_6():
    assert find_lis_length_recursive([-4, 10, 3, 7, 15]) == 4


def test_7():
    assert find_lis_length_recursive([2, 3, 1, 2, 3, 4, 5]) == 5


def test_8():
    assert find_lis_length_recursive([2, 3, 1, 2, 3, 2, 3]) == 3
