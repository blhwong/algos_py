"""
Have pointer begin k steps ahead of second pointer.
When second pointer ends, first pointer will be k from the end
"""

def removeKthNodeFromEnd(head, k):
    curr, offset = head, head
    count = 0
    while count < k:
        offset = offset.next
        count += 1

    if not offset:
        head.value = head.next.value
        head.next = head.next.next
        return

    while offset.next:
        curr = curr.next
        offset = offset.next

    curr.next = curr.next.next
