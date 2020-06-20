"""
Problem Statement #
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
"""

from heapq import *


def find_k_largest_numbers(nums, k):
    result = []

    for i in range(k):
        heappush(result, nums[i])

    for i in range(k, len(nums)):
        num = nums[i]
        if num > result[0]:
            heappushpop(result, num)

    return result
