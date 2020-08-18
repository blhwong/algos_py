"""
         1
     2       3
   4   5   6   7
"""

def maxPathSum(tree):
    def get_max_path(curr):
        if not curr:
            return 0, -float('inf')

        left_max_branch, left_max_path_sum = get_max_path(curr.left)
        right_max_branch, right_max_path_sum = get_max_path(curr.right)
        max_child_sum_branch = max(left_max_branch, right_max_branch)

        value = curr.value
        max_sum_branch = max(value, value + max_child_sum_branch)
        max_sum_root = max(max_sum_branch, value + left_max_branch + right_max_branch)
        max_path_sum = max(left_max_path_sum, right_max_path_sum, max_sum_root)

        return max_sum_branch, max_path_sum


    return get_max_path(tree)[1]
