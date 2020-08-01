from unittest import TestCase, main
from algo_exp.quickselect.main import quickselect


class TestSuite(TestCase):
    def test_1(self):
        array = [8, 5, 2, 9, 7, 6, 3]
        self.assertEqual(quickselect(array, 3), 5)

if __name__ == '__main__':
    main()
