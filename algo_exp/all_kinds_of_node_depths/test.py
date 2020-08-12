from unittest import TestCase, main
from algo_exp.all_kinds_of_node_depths.main import allKindsOfNodeDepths, BinaryTree

eight = BinaryTree(8)
nine = BinaryTree(9)
four = BinaryTree(4)
four.left = eight
four.right = nine
seven = BinaryTree(7)
six = BinaryTree(6)
five = BinaryTree(5)
three = BinaryTree(3)
three.left = six
three.right = seven
two = BinaryTree(2)
two.left = four
two.right = five
one = BinaryTree(1)
one.left = two
one.right = three


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(allKindsOfNodeDepths(one), 26)


if __name__ == '__main__':
    main()
