from algo_exp.square_of_zeroes.main import squareOfZeroes

def test_1():
    matrix = [
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1],
    ]
    assert squareOfZeroes(matrix)

def test_2():
    matrix = [
        [0, 1],
        [0, 0],
    ]
    assert not squareOfZeroes(matrix)
