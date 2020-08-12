def allKindsOfNodeDepths(root):
    def traverse(curr):
        if not curr:
            return 0, 0, 0
        if not curr.left and not curr.right:
            return 0, 0, 1

        left_sum, left_depth, left_count = traverse(curr.left)
        right_sum, right_depth, right_count = traverse(curr.right)

        depth = left_depth + left_count + right_depth + right_count
        depth_sum = left_sum + right_sum + depth
        child_count = left_count + right_count + 1

        return depth_sum, depth, child_count


    return traverse(root)[0]


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
