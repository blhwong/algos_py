from algo_exp.min_height_bst.main import minHeightBst
from data_structures.binary_search_tree import BST

def test_1():
    result = minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22])
    expected = BST(10)
    expected.left = BST(2)
    expected.right = BST(14)
    expected.left.left = BST(1)
    expected.left.right = BST(5)
    expected.left.right.right = BST(7)
    expected.right.left = BST(13)
    expected.right.right = BST(15)
    expected.right.right.right = BST(22)
    assert BST.compare(result, expected) is True
