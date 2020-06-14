"""
Problem Statement #
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

from collections import deque

def traverse(root):
    result = []
    q = deque()
    q.append(root)

    count = 0
    while q:
        curr_level = deque()

        for _ in range(len(q)):
            curr = q.popleft()

            if count % 2 != 0:
                curr_level.appendleft(curr.val)
            else:
                curr_level.append(curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        result.append(list(curr_level))
        count += 1

    return result
