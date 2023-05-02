from grokking.tree_bfs.reverse_level_order_traversal.main import traverse
from data_structures.tree_node import TreeNode as TreeNode


def test_1():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = traverse(root)
    expected = [[9, 10, 5], [7, 1], [12]]
    assert result == expected


def test_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    result = traverse(root)
    expected = [[4, 5, 6, 7], [2, 3], [1]]
    assert result == expected
