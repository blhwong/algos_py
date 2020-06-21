"""
Problem Statement #
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
Example 3:

Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.
"""


def can_partition_recursive(nums):
    def partition(curr_sum, curr_idx, dp):
        if curr_idx >= len(nums):
            return False
        if curr_sum == 0:
            return True

        if dp[curr_idx][curr_sum] is not None:
            return dp[curr_idx][curr_sum]

        if nums[curr_idx] <= curr_sum:
            res = partition(curr_sum - nums[curr_idx], curr_idx + 1, dp)
            if res:
                dp[curr_idx][curr_sum] = res
                return res

        res = partition(curr_sum, curr_idx + 1, dp)
        dp[curr_idx][curr_sum] = res
        return res

    s = sum(nums)

    if s % 2 != 0:
        return False

    dp = [[None] * int((s / 2) + 1) for _ in range(len(nums))]
    return partition(int(s / 2), 0, dp)

def can_partition_iterative(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    s = int(total_sum / 2)

    dp = [[False] * (s + 1) for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    for j in range(1, s + 1):
        dp[0][j] = nums[0] == j

    for i in range(1, len(nums)):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif nums[i] <= j:
                dp[i][j] = dp[i - 1][j - nums[i]]

    return dp[-1][s]


