"""
Problem Statement #
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
"""


def find_paths(root, sum):
    ans = []

    def traverse(curr, path, curr_sum):
        if not curr:
            return

        new_sum = curr_sum + curr.val
        new_path = path + [curr.val]

        if new_sum > sum:
            return

        if new_sum == sum:
            ans.append(new_path)
            return

        traverse(curr.left, new_path, new_sum)
        traverse(curr.right, new_path, new_sum)

    traverse(root, [], 0)

    return ans
