from unittest import TestCase, main
from algo_exp.quicksort.main import quickSort


class TestSuite(TestCase):
    def test_1(self):
        array = [8, 5, 2, 9, 7, 6, 3]
        self.assertListEqual(quickSort(array), [2, 3, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    main()
