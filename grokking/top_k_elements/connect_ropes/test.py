from grokking.top_k_elements.connect_ropes.main import minimum_cost_to_connect_ropes


def test_1():
    assert minimum_cost_to_connect_ropes([1, 3, 11, 5]) == 33

def test_2():
    assert minimum_cost_to_connect_ropes([3, 4, 5, 6]) == 36

def test_3():
    assert minimum_cost_to_connect_ropes([1, 3, 11, 5, 2]) == 42
