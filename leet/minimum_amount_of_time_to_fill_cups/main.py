from heapq import *
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_heap = []
        for a in amount:
            if a > 0:
                heappush(max_heap, -a)

        ans = 0
        while max_heap:
            one = heappop(max_heap)
            two = None
            if max_heap:
                two = heappop(max_heap)

            one += 1
            if -one > 0:
                heappush(max_heap, one)

            if two is not None:
                two += 1
                if -two > 0:
                    heappush(max_heap, two)

            ans += 1

        return ans
