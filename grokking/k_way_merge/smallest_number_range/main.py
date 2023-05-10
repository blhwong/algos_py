"""
Problem Statement #
Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

Example 1:

Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
Example 2:

Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
Output: [9, 12]
Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.

1, 4, 5, 7, 8, 8, 10, 12
1, 4, 5, 7

1, 4, 7, 9, 10, 12, 16
1, 4, 7
"""

from heapq import *

def find_smallest_range(lists):
    left, right = -float('infinity'), float('infinity')
    curr_max = -float('infinity')
    min_heap = []
    for i in range(len(lists)):
        val = lists[i][0]
        curr_max = max(curr_max, val)
        heappush(min_heap, (val, 0, lists[i]))

    while len(min_heap) == len(lists):
        val, curr_idx, l = heappop(min_heap)

        if curr_max - val < right - left:
            left = val
            right = curr_max

        next_idx = curr_idx + 1
        if next_idx < len(l):
            next_val = l[next_idx]
            curr_max = max(curr_max, next_val)
            heappush(min_heap, (next_val, next_idx, l))

    return [left, right]
