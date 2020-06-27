from unittest import TestCase, main
from algo_exp.closest_value_in_bst.main import findClosestValueInBst
from data_structures.tree_node import TreeNode


class TestSuite(TestCase):
    def test_1(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.left.left.left = TreeNode(1)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(22)
        root.right.left.right = TreeNode(14)
        self.assertEqual(findClosestValueInBst(root, 12), 13)


if __name__ == '__main__':
    main()
