"""
Problem Statement #
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
"""


def reverse_every_k_elements(head, k):
    curr, prev = head, None
    while True:
        i = 0
        before_p = prev
        q = curr
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

        q.next = curr

        if not curr:
            break
        prev = q

    return head
