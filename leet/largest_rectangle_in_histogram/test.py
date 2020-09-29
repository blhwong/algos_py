from leet.largest_rectangle_in_histogram.main import Solution


s = Solution()


def test_1():
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10


def test_2():
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3, 1, 1, 1, 1, 1]) == 11
