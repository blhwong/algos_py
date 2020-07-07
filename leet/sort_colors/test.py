from unittest import TestCase, main
from leet.sort_colors.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        i = [2, 0, 2, 1, 1, 0]
        s.sortColors(i)
        self.assertListEqual(i, [0, 0, 1, 1, 2, 2])

    def test_2(self):
        i = [1, 0, 2, 1, 0, 2, 2, 1, 1, 0, 1]
        s.sortColors(i)
        self.assertListEqual(i, [0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2])


if __name__ == '__main__':
    main()
