from unittest import TestCase, main
from grokking.two_pointers.triplet_sum_close_to_target.main import triplet_sum_close_to_target


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(triplet_sum_close_to_target([-2, 0, 1, 2], 2), 1)

    def test_2(self):
        self.assertEqual(triplet_sum_close_to_target([-3, -1, 1, 2], 1), 0)


    def test_3(self):
        self.assertEqual(triplet_sum_close_to_target([1, 0, 1, 1], 100), 3)


if __name__ == '__main__':
    main()
