from unittest import TestCase, main
from grokking.tree_bfs.find_minimum_depth.main import find_minimum_depth
from data_structures.tree_node import TreeNode as TreeNode


class TestSuite(TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(find_minimum_depth(root), 2)

    def test_2(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        self.assertEqual(find_minimum_depth(root), 2)

    def test_3(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.right = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        root.right.left.left = TreeNode(11)
        self.assertEqual(find_minimum_depth(root), 3)





if __name__ == '__main__':
    main()
