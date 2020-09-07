from algo_exp.coin_change_possibilities.main import number_of_ways_to_make_change


def test_1():
    assert number_of_ways_to_make_change(6, [1, 5]) == 2

def test_2():
    assert number_of_ways_to_make_change(10, [1, 5, 10]) == 4

def test_3():
    assert number_of_ways_to_make_change(0, [1, 2, 3]) == 1

def test_4():
    assert number_of_ways_to_make_change(10, []) == 0

def test_5():
    assert number_of_ways_to_make_change(12, [2, 3, 7]) == 4

def test_6():
    assert number_of_ways_to_make_change(7, [2, 3, 4, 7]) == 3
