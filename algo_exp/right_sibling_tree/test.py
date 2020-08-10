from unittest import TestCase, main
from algo_exp.right_sibling_tree.main import rightSiblingTree, BinaryTree

eight = BinaryTree(8)
nine = BinaryTree(9)
ten = BinaryTree(10)
fourteen = BinaryTree(14)
eleven = BinaryTree(11, fourteen)
twelve = BinaryTree(12)
thirteen = BinaryTree(13)
four = BinaryTree(4, eight, nine)
seven = BinaryTree(7, twelve, thirteen)
six = BinaryTree(6, eleven)
five = BinaryTree(5, None, ten)
two = BinaryTree(2, four, five)
three = BinaryTree(3, six, seven)
one = BinaryTree(1, two, three)


class TestSuite(TestCase):
    def test_1(self):
        rightSiblingTree(one)
        self.assertEqual(one.right, None)
        self.assertEqual(two.right, three)
        self.assertEqual(three.right, None)
        self.assertEqual(four.right, five)
        self.assertEqual(five.right, six)
        self.assertEqual(six.right, seven)
        self.assertEqual(seven.right, None)
        self.assertEqual(eight.right, nine)
        self.assertEqual(nine.right, None)
        self.assertEqual(ten.right, eleven)
        self.assertEqual(eleven.right, None)
        self.assertEqual(twelve.right, thirteen)
        self.assertEqual(thirteen.right, None)
        self.assertEqual(fourteen.right, None)



if __name__ == '__main__':
    main()
