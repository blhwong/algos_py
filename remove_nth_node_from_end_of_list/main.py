from data_structures.list_node import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        target = size - n

        if size == 1:
            return None


        size = 0
        curr = head

        prev = None
        while curr:
            if size == target:
                if not prev:
                    head = head.next
                    break
                prev.next = curr.next
                break
            size += 1
            prev = curr
            curr = curr.next

        return head
