from unittest import TestCase, main
from grokking.tree_bfs.level_order_traversal.main import traverse
from data_structures.tree_node import TreeNode as TreeNode


class TestSuite(TestCase):
    def test_1(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)


if __name__ == '__main__':
    main()
