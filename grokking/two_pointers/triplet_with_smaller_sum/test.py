from grokking.two_pointers.triplet_with_smaller_sum.main import triplet_with_smaller_sum, triplet_with_smaller_sum_results


def test_1():
    assert triplet_with_smaller_sum([-1, 0, 2, 3], 3) == 2

def test_2():
    assert triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5) == 4

def test_3():
    assert triplet_with_smaller_sum_results([-1, 0, 2, 3], 3) == [[-1, 0, 3], [-1, 0, 2]]

def test_4():
    assert triplet_with_smaller_sum_results([-1, 4, 2, 1, 3], 5) == [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]
