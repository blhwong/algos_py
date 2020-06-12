from unittest import TestCase, main
from grokking.merge_intervals.merge_intervals.main import merge
from data_structures.interval import Interval


class TestSuite(TestCase):
    def test_1(self):
        intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
        merged = merge(intervals)
        expected = [Interval(1, 5), Interval(7, 9)]
        self.assertTrue(Interval.compare(merged, expected))


    def test_2(self):
        intervals = [Interval(6, 7), Interval(2, 4), Interval(5, 9)]
        merged = merge(intervals)
        expected = [Interval(2, 4), Interval(5, 9)]
        self.assertTrue(Interval.compare(merged, expected))


    def test_3(self):
        intervals = [Interval(1, 4), Interval(2, 6), Interval(3, 5)]
        merged = merge(intervals)
        expected = [Interval(1, 6)]
        self.assertTrue(Interval.compare(merged, expected))


if __name__ == '__main__':
    main()
