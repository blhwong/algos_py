"""
                1
            2       3
        4         6     7
            9
"""

def iterativeInOrderTraversal(tree, callback):
    prev, curr = None, tree

    while curr:
        next_node = None
        if curr.parent == prev:
            if curr.left:
                next_node = curr.left
            else:
                callback(curr)
                next_node = curr.right if curr.right else curr.parent
        elif prev == curr.left:
            callback(curr)
            next_node = curr.right if curr.right else curr.parent
        else:
            next_node = curr.parent

        prev = curr
        curr = next_node
