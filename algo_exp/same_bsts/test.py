from algo_exp.same_bsts.main import sameBsts


def test_1():
    assert sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]) is True

def test_2():
    assert sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 13, 11, 94, 81]) is False
