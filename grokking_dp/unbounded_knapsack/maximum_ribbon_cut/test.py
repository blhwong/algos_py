from grokking_dp.unbounded_knapsack.maximum_ribbon_cut.main import count_ribbon_pieces


def test_1():
    assert count_ribbon_pieces([2, 3, 5], 5) == 2

def test_2():
    assert count_ribbon_pieces([2, 3], 7) == 3

def test_3():
    assert count_ribbon_pieces([3, 5, 7], 13) == 3
