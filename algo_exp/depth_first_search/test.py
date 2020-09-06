from algo_exp.depth_first_search.main import Node


def test_1():
    root = Node('A')
    root.add_child('B')
    root.add_child('C')
    root.add_child('D')
    B = 0
    D = 2
    F = 1
    G = 0
    root.children[B].add_child('E')
    root.children[B].add_child('F')
    root.children[B].children[F].add_child('I')
    root.children[B].children[F].add_child('J')
    root.children[D].add_child('G')
    root.children[D].add_child('H')
    root.children[D].children[G].add_child('K')
    expected = ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
    array = []
    root.depth_first_search(array)
    assert array == expected
