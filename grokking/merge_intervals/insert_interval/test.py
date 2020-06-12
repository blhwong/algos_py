from unittest import TestCase, main
from grokking.merge_intervals.insert_interval.main import insert


class TestSuite(TestCase):
    def test_1(self):
        intervals = [[1, 3], [5, 7], [8, 12]]
        merged = insert(intervals, [4, 6])
        expected = [[1, 3], [4, 7], [8, 12]]
        self.assertCountEqual(merged, expected)

    def test_2(self):
        intervals = [[1, 3], [5, 7], [8, 12]]
        merged = insert(intervals, [4, 10])
        expected = [[1, 3], [4, 12]]
        self.assertCountEqual(merged, expected)

    def test_3(self):
        intervals = [[2, 3], [5, 7]]
        merged = insert(intervals, [1, 4])
        expected = [[1, 4], [5, 7]]
        self.assertCountEqual(merged, expected)


if __name__ == '__main__':
    main()
