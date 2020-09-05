from algo_exp.three_sum.main import three_number_sum


def test_1():
    expected = [
        [-8, 2, 6],
        [-8, 3, 5],
        [-6, 1, 5],
    ]
    assert three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0) == expected
