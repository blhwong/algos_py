from unittest import TestCase, main
from data_structures.tree_node import TreeNode


class TestSuite(TestCase):
    def test_repr(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        expected = '[12, 7, 1, 9, None, 10, 5]'

        self.assertEqual(repr(root), expected)


if __name__ == '__main__':
    main()
