from algo_exp.square_of_zeroes.main import squareOfZeroesBruceForce, squareOfZeroes

class TestBruteForce:
    def test_1(self):
        matrix = [
            [1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 1],
        ]
        assert squareOfZeroesBruceForce(matrix) is True

    def test_2(self):
        matrix = [
            [0, 1],
            [0, 0],
        ]
        assert squareOfZeroesBruceForce(matrix) is False

class TestOptimal:
    def test_1(self):
        matrix = [
            [1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 1],
        ]
        assert squareOfZeroes(matrix) is True

    def test_2(self):
        matrix = [
            [0, 1],
            [0, 0],
        ]
        assert squareOfZeroes(matrix) is False

    def test_3(self):
        matrix = [
            [0, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 1],
        ]
        assert squareOfZeroes(matrix) is False

    def test_4(self):
        matrix = [
            [0, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 1],
        ]
        assert squareOfZeroes(matrix) is True
