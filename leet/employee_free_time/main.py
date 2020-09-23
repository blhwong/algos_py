from heapq import heappush, heappop


class Interval:

    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'[{self.start}, {self.end}]'

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Solution:

    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        merged = []
        min_heap = []

        for i, intervals in enumerate(schedule):
            heappush(min_heap, (intervals[0].start, 0, i, intervals))

        _, i, ec, source = heappop(min_heap)
        first = source[i]
        start, end = first.start, first.end
        if i + 1 < len(source):
            heappush(min_heap, (source[i + 1].start, i + 1, ec, source))

        while min_heap:
            _, i, ec, source = heappop(min_heap)
            curr = source[i]
            if i + 1 < len(source):
                heappush(min_heap, (source[i + 1].start, i + 1, ec, source))
            if curr.start > end:
                merged.append(Interval(start, end))
                start, end = curr.start, curr.end
            else:
                end = max(end, curr.end)

        merged.append(Interval(start, end))

        ans = []

        for i in range(len(merged) - 1):
            if merged[i + 1].start - merged[i].end > 0:
                ans.append(Interval(merged[i].end, merged[i + 1].start))

        return ans
