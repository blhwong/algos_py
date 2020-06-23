from unittest import TestCase, main
from grokking.topological_sort_graph.all_tasks_scheduling_order.main import get_all_orders


class TestSuite(TestCase):
    def test_1(self):
        expected = [[0, 1, 2]]
        self.assertListEqual(get_all_orders(3, [[0, 1], [1, 2]]), expected)

    def test_2(self):
        expected = [
            [3, 2, 0, 1],
            [3, 2, 1, 0]
        ]
        self.assertListEqual(get_all_orders(
            4, [[3, 2], [3, 0], [2, 0], [2, 1]]), expected)

    def test_3(self):
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
        self.assertListEqual(get_all_orders(
            6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]), expected)


if __name__ == '__main__':
    main()
