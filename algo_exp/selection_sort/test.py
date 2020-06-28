from unittest import TestCase, main
from algo_exp.selection_sort.main import selectionSort


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(selectionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])


if __name__ == '__main__':
    main()
