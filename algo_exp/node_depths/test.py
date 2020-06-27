from unittest import TestCase, main
from algo_exp.node_depths.main import nodeDepths
from data_structures.tree_node import TreeNode


class TestSuite(TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(nodeDepths(root), 16)


if __name__ == '__main__':
    main()