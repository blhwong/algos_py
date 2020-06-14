"""
Problem Statement #
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
"""


def reverse_sub_list(head, p, q):
    curr = head
    prev = None
    before_p = None
    i = 0
    while curr and i < p - 1:
        i += 1
        prev = curr
        curr = curr.next

    before_p = prev
    q_node = curr   # the current node is the last node in sublist after reversing

    while curr and i < q:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
        i += 1

    if before_p:
        before_p.next = prev
    else:
        head = prev

    q_node.next = curr

    return head
