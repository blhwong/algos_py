from algo_exp.move_element_to_end.main import move_element_to_end


def test_1():
    assert move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2) == [4, 1, 3, 2, 2, 2, 2, 2]
