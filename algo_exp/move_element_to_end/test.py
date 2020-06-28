from unittest import TestCase, main
from algo_exp.move_element_to_end.main import moveElementToEnd


class TestSuite(TestCase):
    def test_1(self):
        self.assertListEqual(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2), [4, 1, 3, 2, 2, 2, 2, 2])


if __name__ == '__main__':
    main()
