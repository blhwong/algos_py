"""
Problem Statement #
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
"""


def find_sum_of_path_numbers(root):
    return traverse(root, 0)


def traverse(curr, s):
    if curr is None:
        return 0

    new_sum = s * 10 + curr.val

    if curr.left is None and curr.right is None:
        return new_sum

    left = traverse(curr.left, new_sum)
    right = traverse(curr.right, new_sum)

    return left + right
