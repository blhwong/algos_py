from unittest import TestCase, main
from algo_exp.topological_sort.main import topologicalSort


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(topologicalSort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]), [1, 4, 3, 2])

if __name__ == '__main__':
    main()
