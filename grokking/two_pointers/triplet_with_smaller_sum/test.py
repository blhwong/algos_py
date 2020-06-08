from unittest import TestCase, main
from grokking.two_pointers.triplet_with_smaller_sum.main import triplet_with_smaller_sum


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(triplet_with_smaller_sum([-1, 0, 2, 3], 3), 2)

    def test_2(self):
        self.assertEqual(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5), 4)


if __name__ == '__main__':
    main()
