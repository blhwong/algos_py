from algo_exp.disk_stacking.main import diskStacking


def test_1():
    result = diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]])
    expected = [
        [2, 1, 2],
        [3, 2, 3],
        [4, 4, 5],
    ]
    assert result == expected

def test_2():
    result = diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8]])
    expected = [[2, 2, 8]]
    assert result == expected

def test_3():
    result = diskStacking([
        [2, 1, 2],
        [3, 2, 3],
        [2, 2, 8],
        [2, 3, 4],
        [1, 2, 1],
        [4, 4, 5],
        [1, 1, 4]
    ])
    expected = [[1, 1, 4], [2, 2, 8]]
    assert result == expected
