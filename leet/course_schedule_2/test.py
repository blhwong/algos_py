from leet.course_schedule_2.main import Solution


s = Solution()


def test_1():
    assert s.findOrder(2, [[1, 0]]) == [0, 1]


def test_2():
    assert s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]


def test_3():
    assert s.findOrder(1, []) == [0]


def test_4():
    assert s.findOrder(3, [[1, 0], [1, 2], [0, 1]]) == []
