from algo_exp.min_number_of_jumps.main import minNumberOfJumps, minNumberOfJumpsOptimal


def test_1():
    assert minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]) == 4

def test_2():
    assert minNumberOfJumpsOptimal([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]) == 4

def test_3():
    assert minNumberOfJumps([1]) == 0

def test_4():
    assert minNumberOfJumpsOptimal([1]) == 0
