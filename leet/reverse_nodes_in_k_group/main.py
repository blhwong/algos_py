from data_structures.list_node import ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr, prev = head, None
        while curr:
            i = 0
            before_p = prev
            last_reversed_node = curr
            while curr and i < k:
                tmp = curr.next
                prev = curr
                curr = tmp
                i += 1

            if not curr and i < k:
                break

            prev, curr = before_p, last_reversed_node
            i = 0
            while curr and i < k:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                i += 1

            if before_p:
                before_p.next = prev
            else:
                head = prev

            last_reversed_node.next = curr
            prev = last_reversed_node

        return head
