from unittest import TestCase, main
from algo_exp.river_sizes.main import river_sizes


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(river_sizes([
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ]), [1, 2, 2, 2, 5])


if __name__ == '__main__':
    main()
