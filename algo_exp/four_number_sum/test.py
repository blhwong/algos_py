from unittest import TestCase, main
from algo_exp.four_number_sum.main import fourNumberSum, fourSum


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(fourNumberSum([7, 6, 4, -1, 1, 2], 16), [
            [7, 6, 4, -1],
            [7, 6, 1, 2],
        ])

    def test_2(self):
        self.assertCountEqual(fourSum([7, 6, 4, -1, 1, 2], 16), [
            [-1, 4, 6, 7],
            [1, 2, 6, 7],
        ])



if __name__ == '__main__':
    main()
