from grokking.modified_binary_search.order_agnostic_search.main import binary_search


def test_1():
    assert binary_search([4, 6, 10], 10) == 2

def test_2():
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 5) == 4

def test_3():
    assert binary_search([10, 6, 4], 10) == 0

def test_4():
    assert binary_search([10, 6, 4], 4) == 2
