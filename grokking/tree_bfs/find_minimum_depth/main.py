"""
Problem Statement #
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""
from collections import deque

def find_minimum_depth(root):
    q = deque()
    q.append(root)
    level = 0
    while q:
        level_size = len(q)
        level += 1
        for _ in range(level_size):
            curr = q.popleft()
            if curr.left is None and curr.right is None:
                return level
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
