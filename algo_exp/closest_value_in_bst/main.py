def findClosestValueInBst(tree, target):
    def traverse(curr, closest):
        if not curr:
            return closest

        if curr.value == target:
            return target

        compare = abs(curr.value - target)
        if compare < abs(closest - target):
            closest = curr.value

        if curr.value < target:
            return traverse(curr.right, closest)

        return traverse(curr.left, closest)

    return traverse(tree, tree.value)
