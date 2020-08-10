# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def in_order_traverse(curr, array):
    if not curr:
        return array
    in_order_traverse(curr.left, array)
    array.append(curr)
    in_order_traverse(curr.right, array)
    return array


def flattenBinaryTree(root):
    in_order = in_order_traverse(root, [])
    for i, node in enumerate(in_order):
        if i < len(in_order) - 1:
            node.right = in_order[i + 1]
        if i > 1:
            node.left = in_order[i - 1]
    return in_order[0]
