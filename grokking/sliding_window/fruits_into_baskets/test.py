from grokking.sliding_window.fruits_into_baskets.main import fruits_into_baskets


def test_1():
    assert fruits_into_baskets(['A', 'B', 'C', 'A', 'C']) == 3

def test_2():
    assert fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']) == 5

def test_3():
    assert fruits_into_baskets(['A', 'B', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']) == 7
