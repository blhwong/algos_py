from algo_exp.bst_traversal.main import in_order_traverse, pre_order_traverse, post_order_traverse
from data_structures.tree_node import TreeNode

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.right = TreeNode(22)
root.left.left.left = TreeNode(1)


def test_1():
    arr = []
    in_order_traverse(root, arr)
    assert arr == [1, 2, 5, 5, 10, 15, 22]

def test_2():
    arr = []
    pre_order_traverse(root, arr)
    assert arr == [10, 5, 2, 1, 5, 15, 22]

def test_3():
    arr = []
    post_order_traverse(root, arr)
    assert arr == [1, 2, 5, 5, 22, 15, 10]
