from grokking.merge_intervals.intervals_intersection.main import merge


def test_1():
    intervals_a = [[1, 3], [5, 6], [7, 9]]
    intervals_b = [[2, 3], [5, 7]]
    expected = [[2, 3], [5, 6], [7, 7]]
    assert merge(intervals_a, intervals_b) == expected

def test_2():
    intervals_a = [[1, 3], [5, 7], [9, 12]]
    intervals_b = [[5, 10]]
    expected = [[5, 7], [9, 10]]
    assert merge(intervals_a, intervals_b) == expected
