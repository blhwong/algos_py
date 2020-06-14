"""
Problem Statement #
Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.
"""

from collections import deque

def connect_level_order_siblings(root):
    q = deque()
    q.append(root)
    while q:
        prev = None
        for _ in range(len(q)):
            curr = q.popleft()
            if prev:
                prev.next = curr
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

            prev = curr
