from unittest import TestCase, main
from algo_exp.kadanes_algorithm.main import kadanesAlgorithm


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19)

    def test_2(self):
        self.assertEqual(kadanesAlgorithm([-1, -2, -3]), -1)


if __name__ == '__main__':
    main()
