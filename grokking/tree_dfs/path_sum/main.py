"""
Problem Statement #
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
"""


def has_path(root, s):
    return traverse(root, s, 0)

def traverse(curr, s, curr_sum):
    if curr is None:
        return s == curr_sum

    left = traverse(curr.left, s, curr_sum + curr.val)
    right = traverse(curr.right, s, curr_sum + curr.val)

    return left or right
