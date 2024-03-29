"""
Problem Statement #
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

from collections import deque

def traverse(root):
    ans = []
    q = deque()
    q.append(root)
    while q:
        level_size = len(q)
        curr_level = []
        for _ in range(level_size):
            curr = q.popleft()
            curr_level.append(curr.val)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        ans.append(curr_level)

    return ans
