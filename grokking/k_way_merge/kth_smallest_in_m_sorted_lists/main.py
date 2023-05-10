"""
Problem Statement #
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
"""

from heapq import *

def find_Kth_smallest(lists, k):
    min_heap = []
    count = 1

    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))

    while len(min_heap) > 0:
        val, curr_idx, l = heappop(min_heap)
        if count == k:
            return val
        count += 1
        next_idx = curr_idx + 1
        if next_idx < len(l):
            heappush(min_heap, (l[next_idx], next_idx, l))

    return -1
