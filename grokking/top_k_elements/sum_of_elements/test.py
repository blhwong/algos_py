from grokking.top_k_elements.sum_of_elements.main import find_sum_of_elements


def test_1():
    assert find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6) == 23

def test_2():
    assert find_sum_of_elements([3, 5, 8, 7], 1, 4) == 12
