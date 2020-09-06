from algo_exp.spiral_traverse.main import spiral_traverse


def test_1():
    result = spiral_traverse([
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ])
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert result == expected

def test_2():
    assert spiral_traverse([[1]]) == [1]

def test_3():
    result = spiral_traverse([
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ])
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert result == expected
