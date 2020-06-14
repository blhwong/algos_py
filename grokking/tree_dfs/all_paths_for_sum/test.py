from unittest import TestCase, main
from grokking.tree_dfs.all_paths_for_sum.main import find_paths
from data_structures.tree_node import TreeNode as TreeNode


class TestSuite(TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(9)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(7)

        expected = [[1, 7, 4], [1, 9, 2]]
        self.assertListEqual(find_paths(root, 12), expected)


    def test_2(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        expected = [[12, 7, 4], [12, 1, 10]]
        self.assertListEqual(find_paths(root, 23), expected)


if __name__ == '__main__':
    main()
