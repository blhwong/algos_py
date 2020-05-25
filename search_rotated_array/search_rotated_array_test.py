from unittest import TestCase, main
from search_rotated_array import Solution

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.search([4, 5, 6, 7, 0, 1, 2], 0), 4)


    def test_2(self):
        self.assertEqual(s.search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_3(self):
        self.assertEqual(s.search([0, 1, 2, 3, 4, 5, 6], 5), 5)


if __name__ == '__main__':
    main()
