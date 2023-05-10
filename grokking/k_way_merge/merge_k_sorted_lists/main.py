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
    min_heap = []
    count = 0
    for i in range(len(lists)):
        heappush(min_heap, (lists[i].value, count, lists[i]))
        count += 1

    prev = None
    head = None
    while len(min_heap) > 0:
        _, _, curr = heappop(min_heap)
        if curr.next is not None:
            heappush(min_heap, (curr.next.value, count, curr.next))
            count += 1
        if head is None:
            head = curr
        if prev is not None:
            prev.next = curr
        prev = curr

    return head
