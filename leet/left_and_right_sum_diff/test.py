from leet.left_and_right_sum_diff.main import Solution


s = Solution()


def test_1():
    assert s.leftRightDifference([10, 4, 8, 3]) == [15, 1, 11, 22]


def test_2():
    assert s.leftRightDifference([1]) == [0]
