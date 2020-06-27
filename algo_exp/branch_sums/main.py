def branchSums(root):
    ans = []
    def traverse(curr, curr_sum):
        new_sum = curr_sum + curr.value
        if not curr.left and not curr.right:
            ans.append(new_sum)
            return
        if curr.left:
            traverse(curr.left, new_sum)
        if curr.right:
            traverse(curr.right, new_sum)

    traverse(root, 0)
    return ans
