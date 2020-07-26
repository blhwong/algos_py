def shiftLinkedList(head, k):
    size = 0
    curr = head

    while curr:
        curr = curr.next
        size += 1

    end = k % size

    if end == 0:
        return head

    lead_pointer = head
    count = 0
    while lead_pointer and count < end:
        lead_pointer = lead_pointer.next
        count += 1

    curr = head

    while lead_pointer.next:
        lead_pointer = lead_pointer.next
        curr = curr.next


    tmp = curr.next
    curr.next = None
    lead_pointer.next = head

    return tmp
