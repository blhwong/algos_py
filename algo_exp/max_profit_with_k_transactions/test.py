from unittest import TestCase, main
from algo_exp.max_profit_with_k_transactions.main import maxProfitWithKTransactions


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2), 93)


if __name__ == '__main__':
    main()
