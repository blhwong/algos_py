"""
Problem Statement #
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
"""

from heapq import *


def merge_lists(lists):
    ans = None
    min_heap = []
    entry_count = 0

    for root in lists:
        heappush(min_heap, (root.val, entry_count, root))
        entry_count += 1

    head, tail = None, None

    while min_heap:
        val, count, curr = heappop(min_heap)
        if curr.next:
            heappush(min_heap, (curr.next.val, count, curr.next))

        if not head:
            head = curr
            tail = curr
        else:
            tail.next = curr
            tail = tail.next

    return head
