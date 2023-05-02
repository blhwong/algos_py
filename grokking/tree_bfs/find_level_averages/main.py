"""
Problem Statement #
Given a binary tree, populate an array to represent the averages of all of its levels.
"""

from collections import deque

def find_level_averages(root):
    ans = []
    q = deque()
    q.append(root)
    while q:
        level_size = len(q)
        curr_sum = 0
        for _ in range(level_size):
            curr = q.popleft()
            curr_sum += curr.val
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)

        ans.append(curr_sum / level_size)

    return ans
