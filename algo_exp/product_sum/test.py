from unittest import TestCase, main
from algo_exp.product_sum.main import productSum


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]), 12)

    def test_2(self):
        self.assertEqual(productSum([1, 2, 3, 4, 5]), 15)


if __name__ == '__main__':
    main()
