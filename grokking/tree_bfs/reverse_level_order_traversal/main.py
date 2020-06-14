"""
Problem Statement #
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.
"""

from collections import deque

def traverse(root):
    result = deque()
    q = deque()
    q.append(root)

    while q:
        curr_level = []
        for _ in range(len(q)):
            curr = q.popleft()
            curr_level.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        result.appendleft(curr_level)

    return list(result)
