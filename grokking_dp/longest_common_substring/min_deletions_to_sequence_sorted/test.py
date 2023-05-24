from grokking_dp.longest_common_substring.min_deletions_to_sequence_sorted.main import find_minimum_deletions


def test_1():
    assert find_minimum_deletions([4, 2, 3, 6, 10, 1, 12]) == 2


def test_2():
    assert find_minimum_deletions([-4, 10, 3, 7, 15]) == 1


def test_3():
    assert find_minimum_deletions([3, 2, 1, 0]) == 3
