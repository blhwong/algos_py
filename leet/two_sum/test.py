from unittest import TestCase, main
from main import Solution

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual([0, 1], s.twoSum([1, 2, 3, 4, 5], 3))

    def test_2(self):
        self.assertEqual([], s.twoSum([1, 2, 3, 4, 5], 16))

if __name__ == '__main__':
    main()
