"""
Problem Statement #
Design a class to efficiently find the Kth largest element in a stream of numbers.

The class should have the following two things:

The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
The class should expose a function add(int num) which will store the given number and return the Kth largest number.
Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
2. Calling add(4) should still return '6'.
"""

from heapq import *

class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.k = k
        self.min_heap = []

        for i in range(k):
            heappush(self.min_heap, nums[i])

        for i in range(k, len(nums)):
            self.add(nums[i])

    def add(self, num):
        if num > self.min_heap[0]:
            heappushpop(self.min_heap, num)

        return self.min_heap[0]
