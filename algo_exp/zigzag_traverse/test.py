from unittest import TestCase, main
from algo_exp.zigzag_traverse.main import zigzagTraverse


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(zigzagTraverse([
            [1, 3, 4, 10],
            [2, 5, 9, 11],
            [6, 8, 12, 15],
            [7, 13, 14, 16],
        ]), [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
        ])


if __name__ == '__main__':
    main()
