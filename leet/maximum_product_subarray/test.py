from unittest import TestCase, main
from leet.maximum_product_subarray.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(s.maxProduct([2, 3, -2, 4]), 6)

    def test_2(self):
        self.assertEqual(s.maxProduct([-2, 0, -1]), 0)

    def test_3(self):
        self.assertEqual(s.maxProduct([-2, 3, -4]), 24)

    def test_4(self):
        self.assertEqual(s.maxProduct([]), 0)

    def test_5(self):
        self.assertEqual(s.maxProduct([-2]), -2)

if __name__ == '__main__':
    main()
