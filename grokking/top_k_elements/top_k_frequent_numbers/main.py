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
    ans = []
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1

    for num, count in freq.items():
        heappush(ans, (-count, num))

    return [num for idx, (count, num) in enumerate(ans) if idx < k]
