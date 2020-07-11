from unittest import TestCase, main
from algo_exp.single_cycle_check.main import hasSingleCycle


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(hasSingleCycle([2, 3, 1, -4, -4, 2]))

    def test_2(self):
        self.assertFalse(hasSingleCycle([1, 1, 1]))


if __name__ == '__main__':
    main()
