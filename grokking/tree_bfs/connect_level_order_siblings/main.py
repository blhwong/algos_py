"""
Problem Statement #
Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.
"""

from collections import deque

def connect_level_order_siblings(root):
    q = deque()
    q.append(root)
    while q:
        level_size = len(q)
        prev = None
        for _ in range(level_size):
            curr = q.popleft()
            if prev:
                prev.next = curr
            prev = curr
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
