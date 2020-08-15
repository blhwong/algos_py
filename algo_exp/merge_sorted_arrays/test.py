from unittest import TestCase, main
from algo_exp.merge_sorted_arrays.main import mergeSortedArrays


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(mergeSortedArrays([
            [1, 5, 9, 21],
            [-1, 0],
            [-124, 81, 121],
            [3, 6, 12, 20, 150],
        ]), [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150])


if __name__ == '__main__':
    main()
