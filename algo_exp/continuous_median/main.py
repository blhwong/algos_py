# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.

from heapq import *

class ContinuousMedianHandler:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.median = None

    def insert(self, number):
        if not self.min_heap and not self.max_heap:
            heappush(self.min_heap, number)
            self.sync_median()
            return

        size = len(self.min_heap) + len(self.max_heap)

        if size % 2 == 0:
            large, small = -self.max_heap[0], self.min_heap[0]
            if number < large:
                heappush(self.min_heap, -heappop(self.max_heap))
                heappush(self.max_heap, -number)
            else:
                heappush(self.min_heap, number)
        else:
            if number <= self.median:
                heappush(self.max_heap, -number)
            else:
                heappush(self.max_heap, -heappop(self.min_heap))
                heappush(self.min_heap, number)

        self.sync_median()


    def getMedian(self):
        return self.median

    def sync_median(self):
        size = len(self.min_heap) + len(self.max_heap)

        if size % 2 == 0:
            self.median = (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            self.median = self.min_heap[0]
