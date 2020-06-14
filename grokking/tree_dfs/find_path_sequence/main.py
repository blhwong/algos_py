"""
Problem Statement #
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""


def find_path(root, sequence):
    def traverse(curr, idx):
        if not curr:
            return idx == len(sequence)

        if curr.val != sequence[idx]:
            return False

        return (
            traverse(curr.left, idx + 1) or
            traverse(curr.right, idx + 1)
        )

    return traverse(root, 0)
