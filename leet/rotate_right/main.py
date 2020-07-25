from data_structures.list_node import ListNode

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        lead_count = k % count

        if not lead_count:
            return head

        i = 0
        leading_pointer = head
        while i < lead_count:
            i += 1
            leading_pointer = leading_pointer.next

        curr = head
        while leading_pointer.next:
            curr = curr.next
            leading_pointer = leading_pointer.next

        tmp = curr.next
        curr.next = None

        if tmp:
            leading_pointer.next = head
        else:
            tmp = head

        return tmp
