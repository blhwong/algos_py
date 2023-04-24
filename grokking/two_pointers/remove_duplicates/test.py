from grokking.two_pointers.remove_duplicates.main import remove_duplicates


def test_1():
    assert remove_duplicates([2, 3, 3, 3, 6, 9, 9]) == 4

def test_2():
    assert remove_duplicates([2, 2, 2, 11]) == 2
