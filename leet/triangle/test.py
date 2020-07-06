from unittest import TestCase, main
from leet.triangle.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.minimumTotal([
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]), 11)

    def test_2(self):
        self.assertEqual(s.minimumTotal([
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3],
            [100, 100, 100, 5, 2]
        ]), 18)


if __name__ == '__main__':
    main()
