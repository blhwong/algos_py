from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = []
        if not intervals:
            return ans
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr[0] > end:
                ans.append([start, end])
                start, end = curr

            end = max(end, curr[1])

        ans.append([start, end])

        return ans
