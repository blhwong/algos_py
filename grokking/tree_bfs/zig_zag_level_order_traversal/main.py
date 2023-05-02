"""
Problem Statement #
Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.
"""

from collections import deque

def traverse(root):
    ans = []
    q = deque()
    q.append(root)
    i = 0
    while q:
        level_size = len(q)
        curr_level = deque()
        for _ in range(level_size):
            curr = q.popleft()
            if i % 2 == 0:
                curr_level.append(curr.val)
            else:
                curr_level.appendleft(curr.val)

            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)

        ans.append(list(curr_level))
        i += 1

    return ans
