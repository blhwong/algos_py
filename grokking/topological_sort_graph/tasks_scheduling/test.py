from grokking.topological_sort_graph.tasks_scheduling.main import is_scheduling_possible


def test_1():
    assert is_scheduling_possible(3, [[0, 1], [1, 2]])

def test_2():
    assert not is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])

def test_3():
    assert is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
