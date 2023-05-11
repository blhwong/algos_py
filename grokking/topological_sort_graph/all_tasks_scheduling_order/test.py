from grokking.topological_sort_graph.all_tasks_scheduling_order.main import get_all_orders


def test_1():
    expected = [[0, 1, 2]]
    assert get_all_orders(3, [[0, 1], [1, 2]]) == expected

def test_2():
    expected = [
        [3, 2, 0, 1],
        [3, 2, 1, 0]
    ]
    assert get_all_orders(
        4, [[3, 2], [3, 0], [2, 0], [2, 1]]) == expected

def test_3():
    expected = [
        [0, 1, 3, 2, 4, 5],
        [0, 1, 3, 2, 5, 4],
        [0, 1, 3, 4, 2, 5],
        [0, 1, 4, 3, 2, 5],
        [1, 0, 3, 2, 4, 5],
        [1, 0, 3, 2, 5, 4],
        [1, 0, 3, 4, 2, 5],
        [1, 0, 4, 3, 2, 5],
        [1, 3, 0, 2, 4, 5],
        [1, 3, 0, 2, 5, 4],
        [1, 3, 0, 4, 2, 5],
        [1, 3, 2, 0, 4, 5],
        [1, 3, 2, 0, 5, 4],
    ]
    assert get_all_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]) == expected
