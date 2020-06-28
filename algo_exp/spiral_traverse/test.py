from unittest import TestCase, main
from algo_exp.spiral_traverse.main import spiralTraverse


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(spiralTraverse([
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])


if __name__ == '__main__':
    main()
