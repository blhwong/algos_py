from algo_exp.max_path_sum.main import maxPathSum
from data_structures.tree_node import TreeNode


def test_1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    assert maxPathSum(root) == 18
