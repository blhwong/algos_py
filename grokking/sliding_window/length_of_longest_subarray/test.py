from grokking.sliding_window.length_of_longest_subarray.main import length_of_longest_subarray


def test_1():
    assert length_of_longest_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) == 6

def test_2():
    assert length_of_longest_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) == 9
