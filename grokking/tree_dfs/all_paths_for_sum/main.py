"""
Problem Statement #
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
"""


def find_paths(root, s):
    return traverse(root, s, [], [])


def traverse(curr, s, path, ans):
    if curr is None:
        return

    new_path = path + [curr.val]

    if sum(new_path) == s and curr.left is None and curr.right is None:
        ans.append(new_path)
        return

    traverse(curr.left, s, new_path, ans)
    traverse(curr.right, s, new_path, ans)

    return ans
