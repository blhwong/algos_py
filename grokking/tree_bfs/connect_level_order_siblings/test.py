from unittest import TestCase, main
from grokking.tree_bfs.connect_level_order_siblings.main import connect_level_order_siblings
from data_structures.tree_node import TreeNode as TreeNode


class TestSuite(TestCase):
    def test_1(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        connect_level_order_siblings(root)

        self.assertTrue(root.next == None)
        self.assertTrue(root.left.next == root.right)
        self.assertTrue(root.right.next == None)
        self.assertTrue(root.left.left.next == root.right.left)
        self.assertTrue(root.right.left.next == root.right.right)
        self.assertTrue(root.right.right.next == None)


    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        connect_level_order_siblings(root)

        self.assertTrue(root.next == None)
        self.assertTrue(root.left.next == root.right)
        self.assertTrue(root.right.next == None)
        self.assertTrue(root.left.left.next == root.left.right)
        self.assertTrue(root.left.right.next == root.right.left)
        self.assertTrue(root.right.left.next == root.right.right)
        self.assertTrue(root.right.right.next == None)

if __name__ == '__main__':
    main()
