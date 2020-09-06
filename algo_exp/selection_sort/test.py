from algo_exp.selection_sort.main import selection_sort


def test_1():
    assert selection_sort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
