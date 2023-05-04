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
        self.min_heap = [] # right
        self.max_heap = [] # left

    def insert_num(self, num):
        total = len(self.min_heap) + len(self.max_heap)
        if total == 0:
            heappush(self.min_heap, num)
            return


        if total % 2 == 0:
            if num >= self.min_heap[0]:
                heappush(self.min_heap, num)
            else:
                heappush(self.min_heap, -heappop(self.max_heap))
                heappush(self.max_heap, -num)
        else:
            if num <= self.min_heap[0]:
                heappush(self.max_heap, -num)
            else:
                heappush(self.max_heap, -heappop(self.min_heap))
                heappush(self.min_heap, num)

    def find_median(self):
        total = len(self.min_heap) + len(self.max_heap)
        if total < 1:
            return None
        if total % 2 != 0:
            return self.min_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
