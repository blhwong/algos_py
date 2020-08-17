from algo_exp.merge_sorted_arrays.main import mergeSortedArrays


def test_1():
    result = mergeSortedArrays([
        [1, 5, 9, 21],
        [-1, 0],
        [-124, 81, 121],
        [3, 6, 12, 20, 150],
    ])
    expected = [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]
    assert result == expected
