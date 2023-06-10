"""
Problem Statement #
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example 1:

1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5

max  min
[]   []
[]   [3]
[1]  [3]
[0]   [1, 3]
[0, 1] [3, 5]
[0, 1] [3, 4, 5]
[0, 1, 3] [4, 5, 6]
[0, 1, 3] [4, 5, 6, 10]
[0, 1, 3, 4] [5, 6, 10, 10]
[0, 1, 3, 4] [5, 6, 10, 10, 10]
[0, 1, 3, 4, 5] [6, 10, 10, 10, 10]
[0, 1, 3, 4, 5] [6, 10, 10, 10, 10, 10]
[0, 1, 3, 4, 5, 6] [10, 10, 10, 10, 10, 10]
[0, 1, 3, 4, 5, 6] [10, 10, 10, 10, 10, 10, 10]
"""

from heapq import *


class MedianOfAStream:
    def __init__(self):
        self.min_heap = []  # right
        self.max_heap = []  # left

    def insert_num(self, num):
        heappush(self.max_heap, -heappushpop(self.min_heap, num))
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

    def find_median(self):
        if len(self.min_heap) != len(self.max_heap):
            return self.min_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2
