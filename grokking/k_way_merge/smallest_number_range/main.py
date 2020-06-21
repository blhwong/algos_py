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
"""

from heapq import *

def find_smallest_range(lists):
    start, end = -float('inf'), float('inf')
    min_heap = []
    curr_max = -float('inf')

    for l in lists:
        heappush(min_heap, (l[0], 0, l))
        curr_max = max(curr_max, l[0])


    while len(min_heap) == len(lists):
        val, idx, l = heappop(min_heap)
        curr_diff = curr_max - val
        min_diff = end - start
        if curr_diff < min_diff:
            start = val
            end = curr_max

        if idx + 1 < len(l):
            heappush(min_heap, (l[idx + 1], idx + 1, l))
            curr_max = max(curr_max, l[idx + 1])

    return [start, end]
