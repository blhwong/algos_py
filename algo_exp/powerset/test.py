from unittest import TestCase, main
from algo_exp.powerset.main import powerset


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(powerset([1, 2, 3]), [
            [],
            [1],
            [2],
            [3],
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ])


if __name__ == '__main__':
    main()
