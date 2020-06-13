"""
Problem Statement #
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
"""


def reverse_sub_list(head, p, q):
    def reverse(h):
        prev = None
        curr = h
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    curr = head
    prev = None
    before_p = None
    node_q = None
    while curr:
        if curr.val == p:
            before_p = prev
        elif curr.val == q:
            node_q = curr
        prev = curr
        curr = curr.next


    after_q = node_q.next
    node_q.next = None
    rev = reverse(before_p.next)
    before_p.next = rev

    curr = head
    while curr.next:
        curr = curr.next

    curr.next = after_q

    return head
