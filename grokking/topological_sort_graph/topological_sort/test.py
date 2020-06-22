from unittest import TestCase, main
from grokking.topological_sort_graph.topological_sort.main import topological_sort


class TestSuite(TestCase):
    def test_1(self):
        expected = [3, 2, 0, 1]
        self.assertListEqual(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]), expected)

    def test_2(self):
        expected = [4, 2, 3, 0, 1]
        self.assertListEqual(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]), expected)

    def test_3(self):
        expected = [5, 6, 3, 4, 0, 2, 1]
        self.assertListEqual(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]), expected)

if __name__ == '__main__':
    main()
