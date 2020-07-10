from collections import deque

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


def findClosestValueInBstIterative(tree, target):
    q = deque()
    q.append(tree)

    ans = tree.value

    while q:
        curr = q.popleft()
        if not curr:
            continue
        if curr.value == target:
            return target

        if abs(curr.value - target) < abs(ans - target):
            ans = curr.value

        if curr.value < target:
            q.append(curr.right)
        else:
            q.append(curr.left)

    return ans
