from unittest import TestCase, main
from grokking.topological_sort_graph.tasks_scheduling_order.main import find_order


class TestSuite(TestCase):
    def test_1(self):
        expected = [0, 1, 2]
        self.assertListEqual(find_order(3, [[0, 1], [0, 2]]), expected)

    def test_2(self):
        expected = []
        self.assertListEqual(find_order(3, [[0, 1], [1, 2], [2, 0]]), expected)

    def test_3(self):
        expected = [0, 1, 4, 3, 2, 5]
        self.assertListEqual(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]), expected)


if __name__ == '__main__':
    main()
