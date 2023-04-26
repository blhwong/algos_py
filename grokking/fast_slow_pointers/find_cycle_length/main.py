def find_cycle_length(head):
    length = 0
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return calculate_cycle_length(slow)

    return 0

def calculate_cycle_length(pointer):
    length = 1
    curr = pointer.next
    while pointer != curr:
        length += 1
        curr = curr.next
    return length
