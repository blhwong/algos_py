from unittest import TestCase, main
from leet.first_missing_positive.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.firstMissingPositive([1, 2, 0]), 3)

    def test_2(self):
        self.assertEqual(s.firstMissingPositive([3, 4, -1, 1]), 2)

    def test_3(self):
        self.assertEqual(s.firstMissingPositive([7, 8, 9, 11, 12]), 1)

    def test_4(self):
        self.assertEqual(s.firstMissingPositive([2, 1]), 3)

    def test_5(self):
        self.assertEqual(s.firstMissingPositive([0, 2, 2, 4, 0, 1, 0, 1, 3]), 5)

    def test_5(self):
        self.assertEqual(s.firstMissingPositive([]), 1)

if __name__ == '__main__':
    main()
