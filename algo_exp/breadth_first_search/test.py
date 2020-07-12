from unittest import TestCase, main
from algo_exp.breadth_first_search.main import Node


class TestSuite(TestCase):
    def test_1(self):
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
        expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
        array = []
        root.breadthFirstSearch(array)
        self.assertListEqual(array, expected)


if __name__ == '__main__':
    main()
