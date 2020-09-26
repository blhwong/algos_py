from leet.lowest_common_ancestor.main import Solution
from data_structures.tree_node import TreeNode


s = Solution()

three = TreeNode(3)
five = TreeNode(5)
one = TreeNode(1)
six = TreeNode(6)
two = TreeNode(2)
zero = TreeNode(0)
eight = TreeNode(8)
seven = TreeNode(7)
four = TreeNode(4)

root = three
root.left = five
root.right = one
root.left.left = six
root.left.right = two
root.right.left = zero
root.right.right = eight
root.left.right.left = seven
root.left.right.right = four


def test_1():
    assert s.lowestCommonAncestor(root, five, one) == three


def test_2():
    assert s.lowestCommonAncestor(root, five, four) == five
