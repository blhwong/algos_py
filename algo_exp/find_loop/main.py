def findLoop(head):
    slow, fast = head.next, head.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    first, second = head, slow

    while first != second:
        first = first.next
        second = second.next

    return first
