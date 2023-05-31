from pytest import approx
from leet.power.main import Solution


s = Solution()


def test_1():
    assert approx(s.myPow(2.00000, 10)) == 1024.00000


def test_2():
    assert approx(s.myPow(2.10000, 3)) == 9.26100


def test_3():
    assert approx(s.myPow(2.00000, -2)) == 0.25000


def test_4():
    assert approx(s.myPow(0.00001, 2147483647)) == 0
