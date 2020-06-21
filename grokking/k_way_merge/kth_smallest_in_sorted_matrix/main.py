"""
Problem Statement #
Given an N * NN∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

Example 1:

Input: Matrix=[
    [2, 6, 8],
    [3, 7, 10],
    [5, 8, 11]
  ],
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
"""

from heapq import *


def find_Kth_smallest(matrix, k):
    min_heap = []
    for l in matrix:
        heappush(min_heap, (l[0], 0, l))

    ans = -1
    count = 0

    while min_heap and count < k:
        ans, idx, l = heappop(min_heap)
        if idx + 1 < len(l):
            heappush(min_heap, (l[idx + 1], idx + 1, l))
        count += 1
    return ans
