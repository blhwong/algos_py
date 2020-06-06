from leet.data_structures.list_node import ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        head = None
        tail = None
        def add_to_tail(val):
            nonlocal head
            nonlocal tail
            if not head:
                head = ListNode(val)
                tail = head
            else:
                if not head.next:
                    head.next = tail
                tail.next = ListNode(val)
                tail = tail.next



        while curr1 and curr2:
            if curr1.val < curr2.val:
                add_to_tail(curr1.val)
                curr1 = curr1.next
            else:
                add_to_tail(curr2.val)
                curr2 = curr2.next
        if curr1:
            if tail:
                tail.next = curr1
            else:
                return curr1
        elif curr2:
            if tail:
                tail.next = curr2
            else:
                return curr2

        return head
