from algo_exp.depth_first_search.main import Node


def test_1():
    root = Node('A')
    root.addChild('B')
    root.addChild('C')
    root.addChild('D')
    B = 0
    D = 2
    F = 1
    G = 0
    root.children[B].addChild('E')
    root.children[B].addChild('F')
    root.children[B].children[F].addChild('I')
    root.children[B].children[F].addChild('J')
    root.children[D].addChild('G')
    root.children[D].addChild('H')
    root.children[D].children[G].addChild('K')
    expected = ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
    array = []
    root.depthFirstSearch(array)
    assert array == expected
