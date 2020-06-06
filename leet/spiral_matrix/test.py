from unittest import TestCase, main
from leet.spiral_matrix.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected= [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(s.spiralOrder(matrix), expected)

    def test_2(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(s.spiralOrder(matrix), expected)

    def test_3(self):
        matrix = []
        expected = []
        self.assertEqual(s.spiralOrder(matrix), expected)

if __name__ == '__main__':
    main()
