from algo_exp.water_area.main import waterArea


def test_1():
    assert waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]) == 48
