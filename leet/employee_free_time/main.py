class Interval:

    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'[{self.start}, {self.end}]'

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Solution:

    def merge(self, intervals, interval):
        i = 0
        merged = []
        while i < len(intervals) and intervals[i].end < interval.start:
            merged.append(intervals[i])
            i += 1

        start, end = interval.start, interval.end

        if i < len(intervals):
            start = min(start, intervals[i].start)

        for i in range(i, len(intervals)):
            if intervals[i].start > end:
                merged.append(Interval(start, end))
                start, end = intervals[i].start, intervals[i].end
            else:
                end = max(end, intervals[i].end)

        merged.append(Interval(start, end))

        return merged


    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        merged = schedule[0]

        for i in range(1, len(schedule)):
            for interval in schedule[i]:
                merged = self.merge(merged, interval)

        ans = []

        for i in range(len(merged) - 1):
            if merged[i + 1].start - merged[i].end > 0:
                ans.append(Interval(merged[i].end, merged[i + 1].start))

        return ans
