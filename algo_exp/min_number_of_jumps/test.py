from unittest import TestCase, main
from algo_exp.min_number_of_jumps.main import minNumberOfJumps, minNumberOfJumpsOptimal


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]), 4)

    def test_2(self):
        self.assertEqual(minNumberOfJumpsOptimal([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]), 4)

    def test_3(self):
        self.assertEqual(minNumberOfJumps([1]), 0)

    def test_4(self):
        self.assertEqual(minNumberOfJumpsOptimal([1]), 0)

if __name__ == '__main__':
    main()
