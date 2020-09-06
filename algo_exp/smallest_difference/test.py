from algo_exp.smallest_difference.main import smallest_difference


def test_1():
    assert smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]) == [28, 26]
