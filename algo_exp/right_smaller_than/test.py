from algo_exp.right_smaller_than.main import rightSmallerThan

def test_1():
    assert rightSmallerThan([8, 5, 11, -1, 3, 4, 2]) == [5, 4, 4, 0, 1, 1, 0]

def test_2():
    assert rightSmallerThan([0, 1, 1, 2, 3, 5, 8, 13]) == [0, 0, 0, 0, 0, 0, 0, 0]

def test_3():
    assert rightSmallerThan([8, 5, 2, 9, 5, 6, 3]) == [5, 2, 0, 3, 1, 1, 0]
