from unittest import TestCase, main
from grokking.tree_bfs.find_level_averages.main import find_level_averages
from data_structures.tree_node import TreeNode as TreeNode


class TestSuite(TestCase):
    def test_1(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        result = find_level_averages(root)
        expected = [12.0, 4.0, 6.5]
        self.assertListEqual(result, expected)

    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        result = find_level_averages(root)
        expected = [1, 2.5, 5.5]
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    main()
