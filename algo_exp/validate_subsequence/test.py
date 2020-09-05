from algo_exp.validate_subsequence.main import is_valid_subsequence


def test_1():
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]) is True

def test_2():
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 12]) is False

def test_3():
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]) is True
