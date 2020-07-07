from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.value = val
        self.left, self.right, self.next = None, None, None

    def __repr__(self):
        storage = []

        q = deque()
        q.append(self)

        while q:
            curr = q.popleft()
            if not curr:
                storage.append(None)
                continue
            storage.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)

        while storage[-1] == None:
            storage.pop()

        return str(storage)
