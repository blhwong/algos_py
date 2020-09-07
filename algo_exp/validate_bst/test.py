from algo_exp.validate_bst.main import validate_bst
from data_structures.tree_node import TreeNode


def test_1():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(1)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(22)
    root.right.left.right = TreeNode(14)

    assert validate_bst(root) is True

def test_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    assert validate_bst(root) is False

def test_3():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(22)
    root.left.right.right = TreeNode(11)

    assert validate_bst(root) is False

def test_4():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.right = TreeNode(10)
    root.right = TreeNode(15)

    assert validate_bst(root) is False
