from grokking.cyclic_sort.find_duplicate.main import find_duplicate, find_duplicate_cycle


def test_1():
    assert find_duplicate([1, 4, 4, 3, 2]) == 4

def test_2():
    assert find_duplicate([2, 1, 3, 3, 5, 4]) == 3

def test_3():
    assert find_duplicate([2, 4, 1, 4, 4]) == 4

def test_4():
    assert find_duplicate_cycle([1, 4, 4, 3, 2]) == 4

def test_5():
    assert find_duplicate_cycle([2, 1, 3, 3, 5, 4]) == 3

def test_6():
    assert find_duplicate_cycle([2, 4, 1, 4, 4]) == 4
