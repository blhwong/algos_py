def branchSums(root):
    ans = []
    def traverse(curr, curr_sum):
        if not curr:
            return

        new_sum = curr_sum + curr.value

        if not curr.left and not curr.right:
            ans.append(new_sum)

        traverse(curr.left, new_sum)
        traverse(curr.right, new_sum)


    traverse(root, 0)

    return ans
