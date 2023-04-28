"""
Problem Statement #
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
"""


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    prev, curr = None, head

    while curr:
        before_p = prev
        new_q = curr
        i = 0
        while curr is not None and i < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1

        if before_p is not None:
            before_p.next = prev
        else:
            head = prev

        new_q.next = curr
        prev = new_q

    return head
