from unittest import TestCase, main
from algo_exp.water_area.main import waterArea


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]), 48)

if __name__ == '__main__':
    main()
