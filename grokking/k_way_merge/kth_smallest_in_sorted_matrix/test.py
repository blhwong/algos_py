from unittest import TestCase, main
from grokking.k_way_merge.kth_smallest_in_sorted_matrix.main import find_Kth_smallest


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5), 7)

if __name__ == '__main__':
    main()
