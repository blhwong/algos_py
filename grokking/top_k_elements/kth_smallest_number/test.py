from unittest import TestCase, main
from grokking.top_k_elements.kth_smallest_number.main import find_Kth_smallest_number


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3), 5)

    def test_2(self):
        self.assertEqual(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4), 5)

    def test_3(self):
        self.assertEqual(find_Kth_smallest_number([5, 12, 11, -1, 12], 3), 11)

if __name__ == '__main__':
    main()
