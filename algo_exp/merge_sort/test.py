from unittest import TestCase, main
from algo_exp.merge_sort.main import mergeSort


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(mergeSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])


if __name__ == '__main__':
    main()
