def invertBinaryTree(tree):
    def traverse(curr):
        if not curr:
            return

        curr.left, curr.right = curr.right, curr.left
        traverse(curr.left)
        traverse(curr.right)

    traverse(tree)

    return tree
