from unittest import TestCase, main
from leet.four_sum.main import Solution

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(s.fourSum([7, 6, 4, -1, 1, 2], 16), [
            [-1, 4, 6, 7],
            [1, 2, 6, 7],
        ])

    def test_2(self):
        self.assertCountEqual(s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0), [
            [-3, -2, 2, 3],
            [-3, -1, 1, 3],
            [-3, 0, 0, 3],
            [-3, 0, 1, 2],
            [-2, -1, 0, 3],
            [-2, -1, 1, 2],
            [-2, 0, 0, 2],
            [-1, 0, 0, 1],
        ])

    def test_3(self):
        self.assertCountEqual(s.fourSum([0, 0, 0, 0], 0), [[0, 0, 0, 0]])

if __name__ == '__main__':
    main()
