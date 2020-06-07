from unittest import TestCase, main
from grokking.two_pointers.triple_sum_to_zero.main import search_triplets


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(search_triplets(
            [-3, 0, 1, 2, -1, 1, -2]), [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]])

    def test_2(self):
        self.assertCountEqual(search_triplets(
            [-5, 2, -1, -2, 3]), [[-5, 2, 3], [-2, -1, 3]])


if __name__ == '__main__':
    main()
