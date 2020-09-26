from leet.max_length_of_repeated_subarray.main import Solution


s = Solution()


def test_1():
    assert s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3


def test_2():
    assert s.findLength([0, 1, 1, 1, 1], [1, 0, 1, 0, 1]) == 2


def test_3():
    assert s.findLength([1, 0, 0, 0, 1], [1, 0, 0, 1, 1]) == 3
