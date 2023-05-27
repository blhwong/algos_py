from leet.minimum_amount_of_time_to_fill_cups.main import Solution

s = Solution()


def test_1():
    assert s.fillCups([1, 4, 2]) == 4


def test_2():
    assert s.fillCups([5, 4, 4]) == 7


def test_3():
    assert s.fillCups([5, 0, 0]) == 5


def test_4():
    assert s.fillCups([0, 0, 0]) == 0
