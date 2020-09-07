from algo_exp.coin_change_minimum.main import min_number_of_coins_for_change


def test_1():
    assert min_number_of_coins_for_change(6, [1, 5]) == 2

def test_2():
    assert min_number_of_coins_for_change(10, [1, 5, 10]) == 1

def test_3():
    assert min_number_of_coins_for_change(0, [1, 2, 3]) == 0

def test_4():
    assert min_number_of_coins_for_change(10, []) == -1

def test_5():
    assert min_number_of_coins_for_change(12, [2, 3, 7]) == 3

def test_6():
    assert min_number_of_coins_for_change(7, [2, 3, 4, 7]) == 1

def test_7():
    assert min_number_of_coins_for_change(41, [1, 5, 10, 25]) == 4

def test_8():
    assert min_number_of_coins_for_change(7, [1, 5, 10]) == 3

def test_9():
    assert min_number_of_coins_for_change(10, [11]) == -1

def test_10():
    assert min_number_of_coins_for_change(7, [2, 4]) == -1
