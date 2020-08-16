from algo_exp.coin_change_possibilities.main import numberOfWaysToMakeChange


def test_1():
    assert numberOfWaysToMakeChange(6, [1, 5]) == 2

def test_2():
    assert numberOfWaysToMakeChange(10, [1, 5, 10]) == 4

def test_3():
    assert numberOfWaysToMakeChange(0, [1, 2, 3]) == 1

def test_4():
    assert numberOfWaysToMakeChange(10, []) == 0

def test_5():
    assert numberOfWaysToMakeChange(12, [2, 3, 7]) == 4

def test_6():
    assert numberOfWaysToMakeChange(7, [2, 3, 4, 7]) == 3
