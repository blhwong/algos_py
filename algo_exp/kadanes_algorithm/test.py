from algo_exp.kadanes_algorithm.main import kadanesAlgorithm


def test_1():
    assert kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]) == 19

def test_2():
    assert kadanesAlgorithm([-1, -2, -3]) == -1

def test_3():
    assert kadanesAlgorithm([]) == 0

def test_4():
    assert kadanesAlgorithm([-2]) == -2
