from unittest import TestCase, main
from grokking.k_way_merge.kth_smallest_in_m_sorted_lists.main import find_Kth_smallest


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5), 4)

    def test_2(self):
        self.assertEqual(find_Kth_smallest([[5, 8, 9], [1, 7]], 3), 7)

if __name__ == '__main__':
    main()
