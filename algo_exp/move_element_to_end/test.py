from algo_exp.move_element_to_end.main import moveElementToEnd


def test_1():
    assert moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2) == [4, 1, 3, 2, 2, 2, 2, 2]
