"""
Problem Statement #
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
"""

def count_paths(root, S):
    def traverse(curr, curr_sum):
        if not curr:
            return 0

        new_sum = curr_sum + curr.val

        if not curr.left and not curr.right:
            return 1 if new_sum == S else 0

        return (
            traverse(curr.left, new_sum) +
            traverse(curr.right, new_sum) +
            traverse(curr.left, curr_sum) +
            traverse(curr.right, curr_sum)
        )
    return traverse(root, 0)
