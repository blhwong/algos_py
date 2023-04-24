from grokking.two_pointers.make_squares.main import make_squares, make_squares_deque, make_squares_outward


def test_1():
    assert make_squares([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]

def test_2():
    assert make_squares([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]

def test_3():
    assert make_squares([-4, -3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9, 16]

def test_4():
    assert make_squares_deque([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]

def test_5():
    assert make_squares_deque([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]

def test_6():
    assert make_squares_deque([-4, -3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9, 16]

def test_7():
    assert make_squares_outward([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]

def test_8():
    assert make_squares_outward([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]

def test_9():
    assert make_squares_outward([-4, -3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9, 16]
