from leet.edit_distance.main import Solution


s = Solution()


def test_1():
    assert s.minDistance('horse', 'ros') == 3


def test_2():
    assert s.minDistance('intention', 'execution') == 5
