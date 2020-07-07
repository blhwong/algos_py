from unittest import TestCase, main
from algo_exp.bst_construction.main import BST

root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.left.left = BST(2)
root.left.right = BST(5)
root.left.left.left = BST(1)
root.right.left = BST(13)
root.right.right = BST(22)
root.right.left.right = BST(14)


class TestSuite(TestCase):
    def test_1(self):
        root.insert(12)
        self.assertEqual(root.right.left.left.value, 12)

    def test_2(self):
        root.remove(10)
        self.assertEqual(root.value, 12)

    def test_3(self):
        self.assertTrue(root.contains(15))

    def test_4(self):
        self.assertFalse(root.contains(100))

    def test_5(self):
        root.remove(14)
        self.assertIsNone(root.right.left.right)

    def test_6(self):
        single = BST(1)
        single.right = BST(2)
        single.remove(3)
        self.assertEqual(single.value, 1)
        self.assertEqual(single.right.value, 2)


if __name__ == '__main__':
    main()
