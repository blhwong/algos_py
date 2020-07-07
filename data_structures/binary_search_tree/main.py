from collections import deque

class BST:
    def __init__(self, value):
        self.value = value
        self.val = value
        self.left = None
        self.right = None

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


    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
