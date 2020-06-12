from typing import List
from data_structures.list_node import ListNode

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def get_values(l):
            values = []
            curr = l
            while curr:
                values.append(curr.val)
                curr = curr.next
            return values

        head = None
        tail = None

        def add_to_tail(value):
            nonlocal head
            nonlocal tail
            if not head:
                head = ListNode(value)
                tail = head
            else:
                if not head:
                    head.next = tail

                tail.next = ListNode(value)
                tail = tail.next


        all_values = []
        for i in lists:
            values = get_values(i)
            all_values += values

        all_values.sort()

        for i in all_values:
            add_to_tail(i)

        return head
