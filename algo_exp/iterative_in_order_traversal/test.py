from algo_exp.iterative_in_order_traversal.main import iterativeInOrderTraversal
from data_structures.tree_node import TreeNode

one = TreeNode(1)
one.parent = None
two = TreeNode(2)
two.parent = one
three = TreeNode(3)
three.parent = one
four = TreeNode(4)
four.parent = two
six = TreeNode(6)
six.parent = three
seven = TreeNode(7)
seven.parent = three
nine = TreeNode(9)
nine.parent = four
one.left = two
one.right = three
one.left.left = four
one.left.left.right = nine
one.right.left = six
one.right.right = seven


def test_1():
    result = []
    iterativeInOrderTraversal(one, lambda node: result.append(node.val))
    assert result == [4, 9, 2, 1, 6, 3, 7]
