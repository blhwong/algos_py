from unittest import TestCase, main
from data_structures.binary_search_tree.main import BST


class TestSuite(TestCase):
    def test_1(self):
        bst = BST(10)
        bst.insert(2)
        bst.insert(14)
        bst.insert(1)
        bst.insert(5)
        bst.insert(13)
        bst.insert(15)
        bst.insert(7)
        bst.insert(22)
        expected = str([10, 2, 14, 1, 5, 13, 15, None,
                      None, None, 7, None, None, None, 22])
        self.assertEqual(repr(bst), expected)

    def test_compare_true(self):
        bst1 = BST(10)
        bst1.left = BST(1)
        bst1.right = BST(20)

        bst2 = BST(10)
        bst2.left = BST(1)
        bst2.right = BST(20)

        self.assertTrue(BST.compare(bst1, bst2))

    def test_compare_false(self):
        bst1 = BST(10)
        bst1.left = BST(1)
        bst1.right = BST(21)

        bst2 = BST(10)
        bst2.left = BST(1)
        bst2.right = BST(20)

        self.assertFalse(BST.compare(bst1, bst2))




if __name__ == '__main__':
    main()
