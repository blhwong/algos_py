"""
Problem Statement #
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
"""

from heapq import *


def find_k_frequent_numbers(nums, k):
    frequency_map = {}
    for num in nums:
        if num not in frequency_map:
            frequency_map[num] = 0
        frequency_map[num] += 1

    min_heap = []

    for num, freq in frequency_map.items():
        if len(min_heap) < k:
            heappush(min_heap, (freq, num))
        elif freq > min_heap[0][0]:
            heappushpop(min_heap, (freq, num))

    return [num for _, num in min_heap]
