from algo_exp.kadanes_algorithm.main import kadanes_algorithm


def test_1():
    assert kadanes_algorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]) == 19

def test_2():
    assert kadanes_algorithm([-1, -2, -3]) == -1

def test_3():
    assert kadanes_algorithm([]) == 0

def test_4():
    assert kadanes_algorithm([-2]) == -2
