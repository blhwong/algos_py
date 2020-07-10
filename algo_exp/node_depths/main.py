from collections import deque

def nodeDepths(root):
    q = deque()
    q.append((root, 0))

    ans = 0

    while q:
        curr, depth = q.popleft()
        ans += depth
        if curr.left:
            q.append((curr.left, depth + 1))
        if curr.right:
            q.append((curr.right, depth + 1))

    return ans
