from grokking.topological_sort_graph.topological_sort.main import topological_sort


def test_1():
    expected = [3, 2, 0, 1]
    assert topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]) == expected

def test_2():
    expected = [4, 2, 3, 0, 1]
    assert topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]) == expected

def test_3():
    expected = [5, 6, 3, 4, 0, 2, 1]
    assert topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]) == expected
