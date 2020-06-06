from unittest import TestCase, main
from main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertCountEqual(s.merge(intervals), expected)

    def test_2(self):
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertCountEqual(s.merge(intervals), expected)

    def test_3(self):
        intervals = [[1, 4], [0, 4]]
        expected = [[0, 4]]
        self.assertCountEqual(s.merge(intervals), expected)

    def test_4(self):
        intervals = [[1, 4], [0, 1]]
        expected = [[0, 4]]
        self.assertCountEqual(s.merge(intervals), expected)

    def test_4(self):
        intervals = [[1, 4], [0, 0]]
        expected = [[0, 0], [1, 4]]
        self.assertCountEqual(s.merge(intervals), expected)

if __name__ == '__main__':
    main()
