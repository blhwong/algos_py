"""
Problem Statement #
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
"""

def count_paths(root, S):
    return traverse(root, S, 0)

def traverse(curr, S, curr_sum):
    if curr is None:
        return 0

    next_sum = curr_sum + curr.val

    if curr.left is None and curr.right is None and next_sum == S:
        return 1

    left1 = traverse(curr.left, S, next_sum)
    left2 = traverse(curr.left, S, curr_sum)
    right1 = traverse(curr.right, S, next_sum)
    right2 = traverse(curr.right, S, curr_sum)

    return left1 + left2 + right1 + right2

