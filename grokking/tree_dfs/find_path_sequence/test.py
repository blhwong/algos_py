from unittest import TestCase, main
from grokking.tree_dfs.find_path_sequence.main import find_path
from data_structures.tree_node import TreeNode as TreeNode


class TestSuite(TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(9)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(9)

        self.assertTrue(find_path(root, [1, 9, 9]))

    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(5)

        self.assertTrue(find_path(root, [1, 1, 6]))

    def test_3(self):
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(5)

        self.assertFalse(find_path(root, [1, 0, 7]))

if __name__ == '__main__':
    main()
