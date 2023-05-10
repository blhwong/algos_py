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
    for i in range(len(matrix)):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    count = 1
    while len(min_heap) > 0:
        val, curr_idx, l = heappop(min_heap)
        if count == k:
            return val

        count += 1
        next_idx = curr_idx + 1
        if next_idx < len(l):
            heappush(min_heap, (l[next_idx], next_idx, l))

    return -1
