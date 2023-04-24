from grokking.sliding_window.max_sum_subarray_size_k.main import max_sub_array_of_size_k

def test_1():
    assert max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]) == 9

def test_2():
    assert max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]) == 7
