from algo_exp.node_depths.main import node_depths
from data_structures.tree_node import TreeNode


def test_1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert node_depths(root) == 16
