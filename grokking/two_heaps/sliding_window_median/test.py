from grokking.two_heaps.sliding_window_median.main import SlidingWindowMedian


def test_1():
    s = SlidingWindowMedian()
    result = s.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    expected = [1.5, 0.5, 1.0, 4.0]
    assert result == expected

def test_2():
    s = SlidingWindowMedian()
    result = s.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    expected = [1.0, 2.0, 3.0]
    assert result == expected
