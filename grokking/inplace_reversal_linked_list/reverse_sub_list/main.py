"""
Problem Statement #
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

1 -> 2 -> 3 -> 4 -> 5
1 <- 2 <- 3 <- 4
"""


def reverse_sub_list(head, p, q):
    if p == q:
        return head
    prev, curr = None, head
    i = 0
    while curr is not None and i < p - 1:
        prev = curr
        curr = curr.next
        i += 1

    before_p = prev
    new_q = curr

    i = 0
    while curr is not None and i < q - p + 1:
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

    return head
