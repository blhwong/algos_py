from unittest import TestCase, main
from algo_exp.rectangle_mania.main import rectangleMania


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(rectangleMania([
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [2, 1],
            [2, 0],
            [3, 1],
            [3, 0],
        ]), 6)


if __name__ == '__main__':
    main()
