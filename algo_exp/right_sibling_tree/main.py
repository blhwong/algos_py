# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def traverse(curr, parent, is_left_child):
    if not curr:
        return
    left, right = curr.left, curr.right
    traverse(left, curr, True)
    if not parent:
        curr.right = None
    elif is_left_child:
        curr.right = parent.right
    else:
        curr.right = parent.right.left if parent.right else None

    traverse(right, curr, False)

def rightSiblingTree(root):
    traverse(root, None, False)
    return root
