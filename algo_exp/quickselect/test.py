from algo_exp.quickselect.main import quickselect


def test_1():
    array = [8, 5, 2, 9, 7, 6, 3]
    assert quickselect(array, 3) == 5
