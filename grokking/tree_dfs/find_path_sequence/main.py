"""
Problem Statement #
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""


def find_path(root, sequence):
    return traverse(root, sequence, 0)

def traverse(curr, sequence, curr_idx):
    if curr is None:
        return False

    if sequence[curr_idx] != curr.val or curr_idx >= len(sequence):
        return False

    if curr.left is None and curr.right is None and curr_idx + 1 == len(sequence):
        return True

    left = traverse(curr.left, sequence, curr_idx + 1)
    right = traverse(curr.right, sequence, curr_idx + 1)

    return left or right
