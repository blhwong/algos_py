from unittest import TestCase, main
from algo_exp.validate_bst.main import validateBst
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

        self.assertTrue(validateBst(root))

    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertFalse(validateBst(root))

    def test_3(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(22)
        root.left.right.right = TreeNode(11)

        self.assertFalse(validateBst(root))

    def test_4(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.right = TreeNode(10)
        root.right = TreeNode(15)

        self.assertFalse(validateBst(root))



if __name__ == '__main__':
    main()
