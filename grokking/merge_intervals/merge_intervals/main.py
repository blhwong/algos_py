"""
Example 1:

Intervals: [[1, 4], [2, 5], [7, 9]]
Output: [[1, 5], [7, 9]]
Explanation: Since the first two intervals[1, 4] and [2, 5] overlap, we merged them into
one[1, 5].
svg viewer
Example 2:

Intervals: [[6, 7], [2, 4], [5, 9]]
Output: [[2, 4], [5, 9]]
Explanation: Since the intervals[6, 7] and [5, 9] overlap, we merged them into one[5, 9].

Example 3:

Intervals: [[1, 4], [2, 6], [3, 5]]
Output: [[1, 6]]
Explanation: Since all the given intervals overlap, we merged them into one.
"""

from data_structures.interval import Interval


def merge(intervals):
    intervals.sort(key = lambda i: i.start)
    ans = []
    start, end = intervals[0].start, intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start > end:
            ans.append(Interval(start, end))
            start, end = interval.start, interval.end
        else:
            end = max(end, interval.end)

    ans.append(Interval(start, end))

    return ans
