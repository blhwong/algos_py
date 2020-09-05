from algo_exp.four_number_sum.main import four_number_sum


def test_1():
    expected = [
        [-1, 4, 6, 7],
        [1, 2, 6, 7],
    ]
    assert four_number_sum([7, 6, 4, -1, 1, 2], 16) == expected
