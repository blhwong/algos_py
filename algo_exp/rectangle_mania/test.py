from algo_exp.rectangle_mania.main import rectangleMania


def test_1():
    result = rectangleMania([
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0],
        [2, 1],
        [2, 0],
        [3, 1],
        [3, 0],
    ])
    assert result == 6
