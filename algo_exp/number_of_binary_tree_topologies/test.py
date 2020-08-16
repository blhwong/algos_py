from unittest import TestCase, main
from algo_exp.number_of_binary_tree_topologies.main import numberOfBinaryTreeTopologies


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(numberOfBinaryTreeTopologies(3), 5)

    def test_2(self):
        self.assertEqual(numberOfBinaryTreeTopologies(0), 1)


if __name__ == '__main__':
    main()
