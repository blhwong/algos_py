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

    for l in lists:
        start = 0
        heappush(min_heap, (l[0], start, l))

    ans = -1
    count = 0
    while min_heap and count < k:
        val, idx, l = heappop(min_heap)
        ans = val
        next_idx = idx + 1
        if next_idx < len(l):
            heappush(min_heap, (l[next_idx], next_idx, l))

        count += 1

    return ans
