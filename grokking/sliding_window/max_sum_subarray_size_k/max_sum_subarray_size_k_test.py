from unittest import TestCase, main
from max_sum_subarray_size_k import max_sub_array_of_size_k

class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]), 9)

    def test_2(self):
        self.assertEqual(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]), 7)

if __name__ == '__main__':
    main()
