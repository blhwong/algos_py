"""
Problem Statement #
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
"""

from collections import deque

def find_successor(root, key):
    q = deque()
    q.append(root)
    while q:
        curr = q.popleft()
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)

        if curr.val == key:
            break

    return q[0]
