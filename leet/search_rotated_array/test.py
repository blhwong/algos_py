from leet.search_rotated_array.main import Solution

s = Solution()


def test_1():
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_2():
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_3():
    assert s.search([0, 1, 2, 3, 4, 5, 6], 5) == 5


def test_4():
    assert s.search([3, 5, 1], 3) == 0
