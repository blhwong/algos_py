def reverseLinkedList(head):
    curr = head
    prev = None

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev
