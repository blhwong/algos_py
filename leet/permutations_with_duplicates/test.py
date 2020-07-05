from unittest import TestCase, main
from leet.permutations_with_duplicates.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(s.permuteUnique([1, 1, 2, 2]), [[1, 1, 2, 2], [1, 2, 1, 2], [
                         1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]])

    def test_2(self):
        self.assertCountEqual(s.permuteUnique([1, 1, 2]), [
            [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1]
        ])


if __name__ == '__main__':
    main()
