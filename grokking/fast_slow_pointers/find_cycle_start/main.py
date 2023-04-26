def find_cycle_start(head):
    p1 = head
    p2 = head

    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            break

    length = calculate_cycle_length(p1)

    p1, p2 = head, head

    for _ in range(length):
        p2 = p2.next

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1


def calculate_cycle_length(pointer):
    length = 1
    curr = pointer.next
    while curr != pointer:
        length += 1
        curr = curr.next
    return length
