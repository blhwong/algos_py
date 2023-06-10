"""
Problem Statement #
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0
Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0
"""

from heapq import *

class SlidingWindowMedian:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def insert(self, num):
        heappush(self.max_heap, -heappushpop(self.min_heap, num))
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

    def remove(self, num):
        if num >= self.min_heap[0]:
            self.min_heap.remove(num)
            heapify(self.min_heap)
            if len(self.max_heap) > len(self.min_heap):
                heappush(self.min_heap, -heappop(self.max_heap))
        else:
            self.max_heap.remove(-num)
            heapify(self.max_heap)
            if len(self.min_heap) - len(self.max_heap) > 1:
                heappush(self.max_heap, -heappop(self.min_heap))

    def get_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return self.min_heap[0]

    def find_sliding_window_median(self, nums, k):
        ans = []
        start = 0
        for end in range(len(nums)):
            self.insert(nums[end])
            if end + 1 >= k:
                ans.append(self.get_median())
                self.remove(nums[start])
                start += 1

        return ans
