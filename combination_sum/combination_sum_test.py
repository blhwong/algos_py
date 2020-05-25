from unittest import TestCase, main
from combination_sum import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        result = s.combinationSum([2, 3, 6, 7], 7)
        self.assertCountEqual(result, [
            [7],
            [2, 2, 3]
        ])

    def test_2(self):
        result = s.combinationSum([2, 3, 5], 8)
        self.assertCountEqual(result, [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5]
        ])


if __name__ == '__main__':
    main()
