from unittest import TestCase, main
from algo_exp.invert_binary_tree.main import invertBinaryTree
from data_structures.tree_node import TreeNode


class TestSuite(TestCase):
    def test_1(self):
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.right = TreeNode(3)
        tree.left.left = TreeNode(4)
        tree.left.right = TreeNode(5)
        tree.left.left.left = TreeNode(8)
        tree.left.left.right = TreeNode(9)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(7)
        expected = TreeNode(1)
        expected.left = TreeNode(3)
        expected.right = TreeNode(2)
        expected.left.left = TreeNode(7)
        expected.left.right = TreeNode(6)
        expected.right.left = TreeNode(5)
        expected.right.right = TreeNode(4)
        expected.right.right.left = TreeNode(9)
        expected.right.right.right = TreeNode(8)
        result = invertBinaryTree(tree)
        self.assertTrue(TreeNode.compare(result, expected))


if __name__ == '__main__':
    main()
