class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.value = val
        self.next = next

    def __eq__(self, node):
        return self.val == node.val and self.value == node.value and self.next == node.next

    def __repr__(self):
        curr = self

        storage = []
        while curr:
            storage.append(f'{curr.val}')
            curr = curr.next


        return '->'.join(storage)
