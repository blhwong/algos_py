from algo_exp.single_cycle_check.main import has_single_cycle


def test_1():
    assert has_single_cycle([2, 3, 1, -4, -4, 2]) is True

def test_2():
    assert has_single_cycle([2, 1, 1]) is False

def test_3():
    assert has_single_cycle([2, 2, -1]) is True

def test_4():
    assert has_single_cycle([1, 1, 0, 1, 1]) is False

def test_5():
    assert has_single_cycle([1, 1, 1, 1, 2]) is False
