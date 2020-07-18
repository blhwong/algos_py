from unittest import TestCase, main
from algo_exp.min_rewards.main import minRewards


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)


if __name__ == '__main__':
    main()
