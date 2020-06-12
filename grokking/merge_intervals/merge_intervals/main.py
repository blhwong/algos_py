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
    merged = []
    sorted_intervals = sorted(intervals, key=lambda x: x.start)
    start = sorted_intervals[0].start
    end = sorted_intervals[0].end
    for i in range(1, len(sorted_intervals)):
        curr = sorted_intervals[i]
        if curr.start < end:
            end = max(end, curr.end)
        else:
            merged.append(Interval(start, end))
            start = curr.start
            end = curr.end

    merged.append(Interval(start, end))


    return merged
