from unittest import TestCase, main
from smallest_subarray_with_given_sum import smallest_subarray_with_given_sum


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(
            smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]), 2)

    def test_2(self):
        self.assertEqual(
            smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]), 1)


    def test_3(self):
        self.assertEqual(
            smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]), 3)

    def test_4(self):
        self.assertEqual(
            smallest_subarray_with_given_sum(100, [3, 4, 1, 1, 6]), 0)

if __name__ == '__main__':
    main()
