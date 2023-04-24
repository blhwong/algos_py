from grokking.two_pointers.triplet_sum_close_to_target.main import triplet_sum_close_to_target


def test_1():
    assert triplet_sum_close_to_target([-2, 0, 1, 2], 2) == 1

def test_2():
    assert triplet_sum_close_to_target([-3, -1, 1, 2], 1) == 0

def test_3():
    assert triplet_sum_close_to_target([1, 0, 1, 1], 100) == 3

def test_4():
    assert triplet_sum_close_to_target([1, 0, 1, 1, 199, -1, -1], 100) == 3

def test_5():
    assert triplet_sum_close_to_target([1000, 0, 99, 1], 100) == 100

def test_6():
    assert triplet_sum_close_to_target([-10, -9, 8, 1, 2, 100], -20) == -18

def test_7():
    assert triplet_sum_close_to_target([-2, -3, 0, -100, 93], -6) == -7

def test_8():
    assert triplet_sum_close_to_target([1, 2, 3, 10, -1, -1], 7) == 6
