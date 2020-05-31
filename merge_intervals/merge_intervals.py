from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for interval in sorted(intervals, key=lambda a: a[0]):
            if not res:
                res.append(interval)
            else:
                top = res[len(res) - 1]
                left, right = top
                if right < interval[0]:
                    res.append(interval)
                else:
                    top[0] = min(top[0], interval[0])
                    top[1] = max(top[1], interval[1])
        # print(res)
        return res
