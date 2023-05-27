from leet.number_after_double_reversal.main import Solution


s = Solution()


def test_1():
    assert s.isSameAfterReversals(526)


def test_2():
    assert not s.isSameAfterReversals(1800)


def test_3():
    assert s.isSameAfterReversals(0)
