def inOrderTraverse(tree, array):
    def traverse(curr):
        if not curr:
            return
        traverse(curr.left)
        array.append(curr.val)
        traverse(curr.right)

    traverse(tree)
    return array


def preOrderTraverse(tree, array):
    def traverse(curr):
        if not curr:
            return
        array.append(curr.val)
        traverse(curr.left)
        traverse(curr.right)

    traverse(tree)
    return array


def postOrderTraverse(tree, array):
    def traverse(curr):
        if not curr:
            return
        traverse(curr.left)
        traverse(curr.right)
        array.append(curr.val)

    traverse(tree)
    return array
