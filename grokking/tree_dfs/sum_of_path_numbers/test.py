from grokking.tree_dfs.sum_of_path_numbers.main import find_sum_of_path_numbers
from data_structures.tree_node import TreeNode as TreeNode


def test_1():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)

    assert find_sum_of_path_numbers(root) == 408

def test_2():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    assert find_sum_of_path_numbers(root) == 332
