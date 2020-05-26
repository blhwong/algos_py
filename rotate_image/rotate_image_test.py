from unittest import TestCase, main
from rotate_image import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        image = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        s.rotate(image)
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        self.assertListEqual(image, expected)

    def test_2(self):
        image = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        s.rotate(image)
        expected = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
        self.assertListEqual(image, expected)


if __name__ == '__main__':
    main()
