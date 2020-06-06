from unittest import TestCase, main
from main import Solution

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(49, s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

if __name__ == '__main__':
    main()
