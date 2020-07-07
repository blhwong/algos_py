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

if __name__ == '__main__':
    main()
