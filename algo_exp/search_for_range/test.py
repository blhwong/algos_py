from algo_exp.search_for_range.main import searchForRange


def test_1():
    array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
    assert searchForRange(array, 45) == [4, 9]
