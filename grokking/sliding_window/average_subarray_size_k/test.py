from unittest import TestCase, main
from main import average_subarray_size_k


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(
            average_subarray_size_k(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]), [2.2, 2.8, 2.4, 3.6, 2.8])


if __name__ == '__main__':
    main()
