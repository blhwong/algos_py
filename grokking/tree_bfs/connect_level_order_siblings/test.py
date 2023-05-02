from grokking.tree_bfs.connect_level_order_siblings.main import connect_level_order_siblings
from data_structures.tree_node import TreeNode as TreeNode


def test_1():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    connect_level_order_siblings(root)

    assert root.next is None
    assert root.left.next == root.right
    assert root.right.next is None
    assert root.left.left.next == root.right.left
    assert root.right.left.next == root.right.right
    assert root.right.right.next is None


def test_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    connect_level_order_siblings(root)

    assert root.next is None
    assert root.left.next == root.right
    assert root.right.next is None
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.left
    assert root.right.left.next == root.right.right
    assert root.right.right.next is None
