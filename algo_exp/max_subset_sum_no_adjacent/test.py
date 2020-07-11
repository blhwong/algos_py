from unittest import TestCase, main
from algo_exp.max_subset_sum_no_adjacent.main import maxSubsetSumNoAdjacent


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)


if __name__ == '__main__':
    main()
