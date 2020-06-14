"""
Problem Statement #
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""
from collections import deque

def find_minimum_depth(root):
    q = deque()
    q.append(root)
    level = 1
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if not curr.left and not curr.right:
                return level
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        level += 1


    return level
