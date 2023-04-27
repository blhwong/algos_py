from grokking.merge_intervals.insert_interval.main import insert


def test_1():
    intervals = [[1, 3], [5, 7], [8, 12]]
    merged = insert(intervals, [4, 6])
    expected = [[1, 3], [4, 7], [8, 12]]
    assert merged == expected

def test_2():
    intervals = [[1, 3], [5, 7], [8, 12]]
    merged = insert(intervals, [4, 10])
    expected = [[1, 3], [4, 12]]
    assert merged == expected

def test_3():
    intervals = [[2, 3], [5, 7]]
    merged = insert(intervals, [1, 4])
    expected = [[1, 4], [5, 7]]
    assert merged == expected


