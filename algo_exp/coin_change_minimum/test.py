from algo_exp.coin_change_minimum.main import minNumberOfCoinsForChange


def test_1():
    assert minNumberOfCoinsForChange(6, [1, 5]) == 2

def test_2():
    assert minNumberOfCoinsForChange(10, [1, 5, 10]) == 1

def test_3():
    assert minNumberOfCoinsForChange(0, [1, 2, 3]) == 0

def test_4():
    assert minNumberOfCoinsForChange(10, []) == -1

def test_5():
    assert minNumberOfCoinsForChange(12, [2, 3, 7]) == 3

def test_6():
    assert minNumberOfCoinsForChange(7, [2, 3, 4, 7]) == 1

def test_7():
    assert minNumberOfCoinsForChange(41, [1, 5, 10, 25]) == 4

def test_8():
    assert minNumberOfCoinsForChange(7, [1, 5, 10]) == 3

def test_9():
    assert minNumberOfCoinsForChange(10, [11]) == -1

def test_10():
    assert minNumberOfCoinsForChange(7, [2, 4]) == -1
