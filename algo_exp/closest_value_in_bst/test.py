from algo_exp.closest_value_in_bst.main import find_closest_value_in_bst, find_closest_value_in_bst_iterative
from data_structures.tree_node import TreeNode

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(1)
root.right.left = TreeNode(13)
root.right.right = TreeNode(22)
root.right.left.right = TreeNode(14)

def test_1():
    assert find_closest_value_in_bst(root, 12) == 13

def test_2():
    assert find_closest_value_in_bst_iterative(root, 12) == 13
