from unittest import TestCase, main
from algo_exp.three_sum.main import threeNumberSum


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [
            [-8, 2, 6],
            [-8, 3, 5],
            [-6, 1, 5]
        ])


if __name__ == '__main__':
    main()
