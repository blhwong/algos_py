from grokking.topological_sort_graph.alien_dictionary.main import find_order


def test_1():
    expected = [[0, 1, 2]]
    assert find_order(['ba', 'bc', 'ac', 'cab']) == 'bac'

def test_2():
    assert find_order(['cab', 'aaa', 'aab']) == 'cab'

def test_3():
    assert find_order(['ywx', 'wz', 'xww', 'xz', 'zyy', 'zwz']) == 'ywxz'
