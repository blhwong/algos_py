class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.value = val
        self.next = next

    def __repr__(self):
        curr = self

        storage = []
        while curr:
            storage.append(f'{curr.val}')
            curr = curr.next


        return "->".join(storage)

    @staticmethod
    def compare(list1, list2):
        l1 = []
        l2 = []
        curr1 = list1
        while curr1:
            l1.append(curr1.val)
            curr1 = curr1.next

        curr2 = list2
        while curr2:
            l2.append(curr2.val)
            curr2 = curr2.next
        return l1 == l2

