from unittest import TestCase, main
from algo_exp.disk_stacking.main import diskStacking


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]), [
            [2, 1, 2],
            [3, 2, 3],
            [4, 4, 5],
        ])

    def test_2(self):
        self.assertListEqual(diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8]]), [
            [2, 2, 8],
        ])

    def test_3(self):
        self.assertListEqual(diskStacking([
            [2, 1, 2],
            [3, 2, 3],
            [2, 2, 8],
            [2, 3, 4],
            [1, 2, 1],
            [4, 4, 5],
            [1, 1, 4]
        ]), [[1, 1, 4], [2, 2, 8]])

if __name__ == '__main__':
    main()
