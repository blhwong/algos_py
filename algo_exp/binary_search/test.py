from algo_exp.binary_search.main import binary_search


def test_1():
    assert binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33) == 3
