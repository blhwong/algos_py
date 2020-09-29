from algo_exp.search_in_sorted_matrix.main import search_in_sorted_matrix


def test_1():
    result = search_in_sorted_matrix([
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ], 44)
    assert result == [3, 3]
