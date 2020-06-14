"""
Problem Statement #
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
"""


def has_path(root, sum):
    def traverse(curr, curr_sum):
        if not curr:
            return False

        new_sum = curr_sum + curr.val

        if new_sum > sum:
            return False
        if new_sum == sum:
            return True

        return (
            traverse(curr.left, new_sum) or
            traverse(curr.right, new_sum)
        )

    return traverse(root, 0)
