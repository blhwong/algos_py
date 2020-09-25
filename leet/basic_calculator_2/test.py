from leet.basic_calculator_2.main import Solution


s =  Solution()


def test_1():
    assert s.calculate('3+2*2') == 7


def test_2():
    assert s.calculate(' 3/2 ') == 1


def test_3():
    assert s.calculate(' 3+5 / 2') == 5


def test_4():
    assert s.calculate('0') == 0


def test_5():
    assert s.calculate('3 + 5') == 8


def test_6():
    assert s.calculate('1-1+1') == 1


def test_7():
    assert s.calculate('0-1') == -1


def test_8():
    assert s.calculate('3/2 + 3/2') == 2


def test_9():
    assert s.calculate('14-3/2') == 13
