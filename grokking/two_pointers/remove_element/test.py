from grokking.two_pointers.remove_element.main import remove_element


def test_1():
    assert remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3) == 4


def test_2():
    assert remove_element([2, 11, 2, 2, 1], 2) == 2
