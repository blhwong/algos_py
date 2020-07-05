from unittest import TestCase, main
from leet.minimum_path_sum.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.minPathSum([
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]), 7)

    def test_2(self):
        self.assertEqual(s.minPathSum([
            [1, 3, 3, 10],
            [1, 5, 1, 10],
            [4, 2, 1, 10],
            [1, 1, 1, 1]
        ]), 10)


if __name__ == '__main__':
    main()
