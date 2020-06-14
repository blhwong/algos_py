from unittest import TestCase, main
from grokking.tree_dfs.count_paths_for_sum.main import count_paths
from data_structures.tree_node import TreeNode as TreeNode


class TestSuite(TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(9)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(3)

        self.assertEqual(count_paths(root, 12), 3)

    def test_2(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        self.assertEqual(count_paths(root, 11), 2)

    def test_3(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        root.right.right.right = TreeNode(6)

        self.assertEqual(count_paths(root, 11), 3)

if __name__ == '__main__':
    main()
