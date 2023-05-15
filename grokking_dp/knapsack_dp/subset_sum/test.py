from grokking_dp.knapsack_dp.subset_sum.main import has_sum


def test_1():
    assert has_sum([1, 2, 3, 7], 6)

def test_2():
    assert has_sum([1, 2, 7, 1, 5], 10)

def test_3():
    assert not has_sum([1, 3, 4, 8], 6)
