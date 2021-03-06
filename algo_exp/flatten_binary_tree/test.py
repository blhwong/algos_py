from algo_exp.flatten_binary_tree.main import flattenBinaryTree, BinaryTree

four = BinaryTree(4)
seven = BinaryTree(7)
eight = BinaryTree(8)
six = BinaryTree(6)
five = BinaryTree(5, seven, eight)
two = BinaryTree(2, four, five)
three = BinaryTree(3, six)
one = BinaryTree(1, two, three)

def test_1():
    left_to_right = []
    right_to_left = []
    result = flattenBinaryTree(one)
    curr = result
    while curr.right:
        left_to_right.append(curr.value)
        curr = curr.right
    left_to_right.append(curr.value)
    while curr:
        right_to_left.append(curr.value)
        curr = curr.left

    assert left_to_right == [4, 2, 7, 5, 8, 1, 6, 3]
    assert right_to_left == [3, 6, 1, 8, 5, 7, 2, 4]
