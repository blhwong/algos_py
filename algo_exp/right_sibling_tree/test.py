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


def test_1():
    rightSiblingTree(one)
    assert one.right == None
    assert two.right == three
    assert three.right == None
    assert four.right == five
    assert five.right == six
    assert six.right == seven
    assert seven.right == None
    assert eight.right == nine
    assert nine.right == None
    assert ten.right == eleven
    assert eleven.right == None
    assert twelve.right == thirteen
    assert thirteen.right == None
    assert fourteen.right == None
