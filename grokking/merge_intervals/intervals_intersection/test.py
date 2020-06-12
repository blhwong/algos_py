from unittest import TestCase, main
from grokking.merge_intervals.intervals_intersection.main import merge


class TestSuite(TestCase):
    def test_1(self):
        intervals_a = [[1, 3], [5, 6], [7, 9]]
        intervals_b = [[2, 3], [5, 7]]
        expected = [[2, 3], [5, 6], [7, 7]]
        self.assertCountEqual(merge(intervals_a, intervals_b), expected)

    def test_2(self):
        intervals_a = [[1, 3], [5, 7], [9, 12]]
        intervals_b = [[5, 10]]
        expected = [[5, 7], [9, 10]]
        self.assertCountEqual(merge(intervals_a, intervals_b), expected)


if __name__ == '__main__':
    main()
