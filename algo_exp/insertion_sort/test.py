from algo_exp.insertion_sort.main import insertion_sort


def test_1():
    assert insertion_sort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
