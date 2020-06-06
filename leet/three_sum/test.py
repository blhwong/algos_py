from unittest import TestCase, main
from leet.three_sum.main import Solution

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual([
            [-1, 0, 1],
            [-1, -1, 2]
        ], s.threeSum([-1, 0, 1, 2, -1, -4]))

    def test_2(self):
        self.assertListEqual([], s.threeSum([1, 2, 3, 4, 5, 6]))

    def test_3(self):
        self.assertListEqual([], s.threeSum([-1, -2, -3, -4]))

    def test_4(self):
        self.assertListEqual([[0, 0, 0]], s.threeSum([0, 0, 0, 1]))

if __name__ == '__main__':
    main()
