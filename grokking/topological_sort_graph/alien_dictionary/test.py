from unittest import TestCase, main
from grokking.topological_sort_graph.alien_dictionary.main import find_order


class TestSuite(TestCase):
    def test_1(self):
        expected = [[0, 1, 2]]
        self.assertEqual(find_order(['ba', 'bc', 'ac', 'cab']), 'bac')

    def test_2(self):
        self.assertEqual(find_order(['cab', 'aaa', 'aab']), 'cab')

    def test_3(self):
        self.assertEqual(find_order(['ywx', 'wz', 'xww', 'xz', 'zyy', 'zwz']), 'ywxz')


if __name__ == '__main__':
    main()
