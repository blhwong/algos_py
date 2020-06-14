"""
Problem Statement #
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
"""


def find_sum_of_path_numbers(root):
    def traverse(curr, curr_sum):
        if not curr:
            return 0

        new_sum = curr_sum * 10 + curr.val

        if not curr.left and not curr.right:
            return new_sum

        return (
            traverse(curr.left, new_sum) +
            traverse(curr.right, new_sum)
        )

    return traverse(root, 0)
