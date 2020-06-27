from unittest import TestCase, main
from algo_exp.branch_sums.main import branchSums
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
        root.left.right.left = TreeNode(10)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertListEqual(branchSums(root), [15, 16, 18, 10, 11])


if __name__ == '__main__':
    main()
