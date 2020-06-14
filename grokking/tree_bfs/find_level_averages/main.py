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
        curr_sum = 0
        curr_len = len(q)
        for _ in range(curr_len):
            curr = q.popleft()
            curr_sum += curr.val
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        ans.append(curr_sum / curr_len)
    return ans
