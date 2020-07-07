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

    @staticmethod
    def compare(root1, root2):
        def traverse(curr1, curr2):
            if not curr1 and not curr2:
                return True
            if not curr1 and curr2:
                return False
            if curr1 and not curr2:
                return False

            if curr1.val != curr2.val:
                return False

            return traverse(curr1.left, curr2.left) and traverse(curr1.right, curr2.right)

        return traverse(root1, root2)
