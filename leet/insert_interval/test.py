from unittest import TestCase, main
from main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        intervals = [[1, 3], [6, 9]]
        expected = [[1, 5], [6, 9]]
        self.assertCountEqual(s.insert(intervals, [2, 5]), expected)

    def test_2(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        expected = [[1, 2], [3, 10], [12, 16]]
        self.assertCountEqual(s.insert(intervals, [4, 8]), expected)


if __name__ == '__main__':
    main()
