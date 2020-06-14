from unittest import TestCase, main
from grokking.tree_bfs.find_successor.main import find_successor
from data_structures.tree_node import TreeNode as TreeNode


class TestSuite(TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(find_successor(root, 3).val, 4)

    def test_2(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.right = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        self.assertEqual(find_successor(root, 9).val, 10)

    def test_3(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.right = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        root.right.left.left = TreeNode(11)
        self.assertEqual(find_successor(root, 12).val, 7)


if __name__ == '__main__':
    main()
