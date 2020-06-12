from unittest import TestCase, main
from data_structures.interval import Interval


class TestSuite(TestCase):
    def test_compare_same(self):
        intervals1 = []
        intervals2 = []

        intervals1.append(Interval(1, 2))
        intervals1.append(Interval(3, 4))
        intervals1.append(Interval(10, 15))

        intervals2.append(Interval(1, 2))
        intervals2.append(Interval(3, 4))
        intervals2.append(Interval(10, 15))

        self.assertTrue(Interval.compare(intervals1, intervals2))


    def test_compare_different_length(self):
        intervals1 = []
        intervals2 = []

        intervals1.append(Interval(1, 2))
        intervals1.append(Interval(3, 4))
        intervals1.append(Interval(10, 15))

        intervals2.append(Interval(1, 2))
        intervals2.append(Interval(3, 4))

        self.assertFalse(Interval.compare(intervals1, intervals2))


    def test_compare_different_values(self):
        intervals1 = []
        intervals2 = []

        intervals1.append(Interval(1, 2))
        intervals1.append(Interval(3, 4))
        intervals1.append(Interval(10, 15))

        intervals2.append(Interval(2, 4))
        intervals2.append(Interval(3, 6))
        intervals2.append(Interval(10, 15))

        self.assertFalse(Interval.compare(intervals1, intervals2))


if __name__ == '__main__':
    main()
