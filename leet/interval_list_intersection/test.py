from leet.interval_list_intersection.main import Solution


s = Solution()


def test_1():
    result = s.intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]],
    )
    assert result == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]


def test_2():
    result = s.intervalIntersection(
        [[3, 5], [9, 20]],
        [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]],
    )
    assert result == [[4, 5], [9, 10], [11, 12], [14, 15], [16, 20]]
