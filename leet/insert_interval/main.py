from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        i, start, end = 0, 0, 1
        ans = []

        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            ans.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            i += 1

        ans.append(newInterval)

        while i < len(intervals):
            ans.append(intervals[i])
            i += 1

        return ans
