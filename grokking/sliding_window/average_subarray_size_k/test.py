from grokking.sliding_window.average_subarray_size_k.main import average_subarray_size_k


def test_1():
    assert average_subarray_size_k(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]) == [2.2, 2.8, 2.4, 3.6, 2.8]
