def validateBst(tree):
    def traverse(curr, curr_max, curr_min):
        if not curr:
            return True

        if curr.left and not curr.left.value < curr.value:
            return False

        if curr.right and not curr.value <= curr.right.value:
            return False

        if not curr_min <= curr.value < curr_max:
            return False

        return traverse(curr.left, curr.value, curr_min) and traverse(curr.right, curr_max, curr.value)


    return traverse(tree, float('inf'), -float('inf'))
